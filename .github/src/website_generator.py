import os
import re

from bs4 import BeautifulSoup

from html_tools import wrap_tag, html_link, table_to_html
from utils import req_get
from year import Year


URL_PREFIX = 'https://github.com/npanuhin/Advent-of-Code/tree/master'


soup = BeautifulSoup(req_get('https://adventofcode.com/2015/events').text, 'lxml')
YEARS = [
    int(item.find('a').text.removeprefix('[').removesuffix(']'))
    for item in soup.find('body').find('main').find_all('div', class_='eventlist-event')
]


def gen_global_page(solved: dict[int, Year], html_path: str):
    if not os.path.isfile(html_path):
        print('WARNING! Global HTML not found!')
        return
    print('Generating global HTML table...')

    list_items = [
        wrap_tag('li', (
            html_link(f'[{year_num}]', year_num) if year_num in solved else f'[{year_num}]'
        ))
        for year_num in YEARS
    ]

    with open(html_path, encoding='utf-8') as file:
        page = file.read()

    page = re.sub(
        r'(\t+)<ul\s+class="year_list">.*?</ul>',  # \1 - original padding of ul
        r'\1<ul class="year_list">{}\n\1</ul>'.format(
            ''.join(rf'\n\1\t{item}' for item in list_items)
        ),
        page,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(page)


def gen_year_page(year: Year, html_path: str):
    if not os.path.isfile(html_path):
        print(f'WARNING! Year {year.year} HTML not found!')
        return
    print(f'Generating HTML table for year {year.year}...')

    table = []
    for day in year.days:
        tag_args = {'class': 'readme'} if day.readme_exists else {}
        line = [html_link(f'Day {day.day}', f'{URL_PREFIX}/{year.year}/{day.url_name}', tag_args)]

        part_1 = part_2 = None

        if day.day == 25:
            if day.part1_solved:  # and not day.part2_solved:
                part_1 = html_link('⭐⭐', f'{URL_PREFIX}/{year.year}/{day.url_name}/part1.py')
            line.append([part_1, {'colspan': '2'}])

        else:
            if day.part1_solved:
                part_1 = html_link('⭐', f'{URL_PREFIX}/{year.year}/{day.url_name}/part1.py')
            if day.part2_solved:
                part_2 = html_link('⭐', f'{URL_PREFIX}/{year.year}/{day.url_name}/part2.py')
            line.append(part_1)
            line.append(part_2)

        table.append(line)

    table_center, table_right = table[:13], table[13:]

    table_center = wrap_tag('div', table_to_html(table_center), inline=False, tag_args={'class': 'center'})
    table_right = wrap_tag('div', table_to_html(table_right), inline=False, tag_args={'class': 'right'})

    with open(html_path, encoding='utf-8') as file:
        page = file.read()

    page = re.sub(
        r'(\t+)<div class="center">.*?</div>',  # \1 - original padding of div
        '\n'.join(rf'\1{line}' for line in table_center.splitlines()),
        page,
        flags=re.IGNORECASE | re.DOTALL
    )

    page = re.sub(
        r'(\t+)<div class="right">.+?</div>',  # \1 - original padding of div
        '\n'.join(rf'\1{line}' for line in table_right.splitlines()),
        page,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(page)
