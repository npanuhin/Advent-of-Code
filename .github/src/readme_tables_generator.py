from bs4 import BeautifulSoup
from os.path import isfile
import requests
import re

from src.html import table_to_html, html_link
from src.utils import md_link
from src.year import Year


def table2md(table):
    columns_num = len(table[0])
    markdown = [[]]

    # Precalculate table column sizes
    column_sizes = [
        max(len(line[column]) for line in table)
        for column in range(columns_num)
    ]

    # Header
    for column in range(columns_num):
        markdown[-1].append(' {:^{}} '.format(
            table[0][column],
            column_sizes[column] + (column != 0 and '⭐' not in table[0][column])  # Asjustment for ⭐ symbol
        ))

    # Header separator
    markdown.append([
        ':' + '-' * (column_size + (2 if column == 0 else 1)) + ':'
        for column, column_size in enumerate(column_sizes)
    ])
    markdown[-1][0] = markdown[-1][0].strip(':')

    # Table content
    for line in range(1, len(table)):
        markdown.append([
            ' {:<{}} '.format(
                table[line][column],
                column_sizes[column] + (column != 0 and '⭐' not in table[line][column])  # Asjustment for ⭐ symbol
            )
            for column in range(columns_num)
        ])

    # Build table from lines
    return '\n'.join('|{}|'.format('|'.join(line)) for line in markdown)


def gen_global_table(readme_path, solved):
    print('Generating global README table...')
    if not isfile(readme_path):
        return

    table = [['']] + [['Day {}'.format(day + 1)] for day in range(25)]

    for year in solved:
        table[0].append(md_link(year, year))
        for day in range(25):
            day_url_name = 'Day%20{:02d}'.format(day + 1)

            if solved[year][day][2]:
                # Day has README (both parts solved)
                table[day + 1].append(md_link('⭐⭐', '{}/{}'.format(year, day_url_name)))

            elif day + 1 == 25 and solved[year][day][0] and not solved[year][day][1]:
                # This is the 25th day, which can provide both starts for solving the only part
                table[day + 1].append(md_link('⭐⭐', '{}/{}/part1.py'.format(year, day_url_name)))

            else:
                table[day + 1].append(
                    (md_link('⭐', '{}/{}/part1.py'.format(year, day_url_name)) if solved[year][day][0] else '') +
                    (md_link('⭐', '{}/{}/part2.py'.format(year, day_url_name)) if solved[year][day][1] else '')
                )

    # with open(readme_path, 'r', encoding='utf-8') as file:
    #     readme = file.read()

    # readme = re.sub(
    #     REGEX['solved_table'],
    #     lambda match: match.group(1) + '\n' + table2md(table) + '\n' + match.group(2),
    #     readme,
    #     flags=re.IGNORECASE | re.DOTALL
    # )

    # with open(readme_path, 'w', encoding='utf-8') as file:
    #     file.write(readme)


def gen_year_table(year: Year):
    if not year.solved:
        return
    print(f'Generating README table for year {year.year}...')

    table = [[None, 'Part 1', 'Part 2']]

    for day in year.days:
        aoc_page = requests.get(f'https://adventofcode.com/{year.year}/day/{day.day}')
        assert aoc_page.status_code == 200, f'Day {day.day} page is not available'
        soup = BeautifulSoup(aoc_page.text, 'lxml')

        day_name = soup.find('body').find('main').find('article', class_='day-desc').find('h2').text.strip()
        day_name = day_name.strip('-').strip()

        if day.readme_exists:
            line = [html_link(day_name, f'Day%20{day.day:02d}')]
        else:
            line = [day_name]

        part_1 = part_2 = None

        if day.day == 25:
            if day.part1_solved:  # and not day.part2_solved:
                part_1 = html_link('⭐⭐', f'Day%20{day.day:02d}/part1.py')
            line.append([part_1, {'align': 'center', 'colspan': '2'}])

        else:
            if day.part1_solved:
                part_1 = html_link('⭐', f'Day%20{day.day:02d}/part1.py')
            if day.part2_solved:
                part_2 = html_link('⭐', f'Day%20{day.day:02d}/part2.py')
            line.append([part_1, {'align': 'center'}])
            line.append([part_2, {'align': 'center'}])

        table.append(line)

    with open(year.readme_path, 'r', encoding='utf-8') as file:
        readme = file.read()

    readme = re.sub(
        r'(<!-- Solved table start -->).+(<!-- Solved table end -->)',
        lambda match: match.group(1) + '\n' + table_to_html(table, headers_on=True) + '\n' + match.group(2),
        readme,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(year.readme_path, 'w', encoding='utf-8') as file:
        file.write(readme)
