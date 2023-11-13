from bs4 import BeautifulSoup
import os
import re

from src.html import wrap_tag, html_link
from src.utils import req_get
from src.year import Year


soup = BeautifulSoup(req_get('https://adventofcode.com/2015/events').text, 'lxml')
YEARS = [
    int(item.find('a').text.lstrip('[').rstrip(']'))
    for item in soup.find('body').find('main').find_all('div', class_='eventlist-event')
]


def gen_global_page(solved: dict[int, Year], html_path: str):
    if not os.path.isfile(html_path):
        return
    print('Generating global HTML table...')

    list_items = [
        wrap_tag('li', (
            html_link(f'[{year_num}]', year_num) if year_num in solved else f'[{year_num}]'
        ))
        for year_num in YEARS
    ]

    with open(html_path, 'r', encoding="utf-8") as file:
        page = file.read()

    page = re.sub(
        r'(\t+)<ul\s+class="year_list">.+?</ul>',  # \1 -- original padding of ul
        r'\1<ul class="year_list">{}\n\1</ul>'.format(
            ''.join(rf'\n\1\t{item}' for item in list_items)
        ),
        page,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(html_path, 'w', encoding="utf-8") as file:
        file.write(page)


def gen_year_page(year: Year, html_path: str):
    if not os.path.isfile(html_path):
        return
    print(f'Generating HTML table for year {year.year}...')

    table = [
        ['\t' + line.format(year=year, day=day + 1) for line in (
            "<tr>",
            "\t<td>",
            (
                '\t\t<a href="https://github.com/npanuhin/Advent-of-Code/tree/master/{year}/Day%20{day:02d}">Day {day}</a>'
            ),
            "\t</td>",
            '\t' + ('<td colspan="2">' if day + 1 == 25 and not solved[day][1] else "<td>"),
            (
                (
                    '\t\t<a href="https://github.com/npanuhin/Advent-of-Code/tree/master/{year}/Day%20{day:02d}/part1.py">' +
                    ('⭐⭐' if day + 1 == 25 and solved[day][0] and not solved[day][1] else '⭐') +
                    '</a>'
                )
                if solved[day][0] else ""
            ),
            "\t</td>",
            *((
                "\t<td>",
                (
                    '\t\t<a href="https://github.com/npanuhin/Advent-of-Code/tree/master/{year}/Day%20{day:02d}/part2.py">⭐</a>'
                    if solved[day][1] else ""
                ),
                "\t</td>"
            ) if day + 1 != 25 or solved[day][1] else tuple()),
            "</tr>"
        )]
        for day in range(25)
    ]

    table_center = ["<table>"] + sum(table[:13], []) + ["</table>"]
    table_right = ["<table>"] + sum(table[13:], []) + ["</table>"]

    with open(html_path, 'r', encoding="utf-8") as file:
        page = file.read()

    page = re.sub(
        r"(\t+)<div class=\"center\">.+?</div>",
        r'\1<div class="center">\n{}\n\1</div>'.format('\n'.join(r'\1' + '\t' + line for line in table_center)),
        page,
        flags=re.IGNORECASE | re.DOTALL
    )

    page = re.sub(
        r"(\t+)<div class=\"right\">.+?</div>",
        r'\1<div class="right">\n{}\n\1</div>'.format('\n'.join(r'\1' + '\t' + line for line in table_right)),
        page,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(html_path, 'w', encoding="utf-8") as file:
        file.write(page)
