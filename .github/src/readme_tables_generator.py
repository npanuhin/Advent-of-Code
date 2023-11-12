from bs4 import BeautifulSoup
import requests
import os
import re

from src.html import table_to_html, html_link
from src.year import Year


def gen_global_table(solved: list[Year], readme_path):
    if not os.path.isfile(readme_path):
        return
    print('Generating global README table...')

    table = [[None]] + [[f'Day {day_num + 1}'] for day_num in range(25)]

    for year in solved:
        table[0].append((html_link(year.year, year.year), {'align': 'center'}))

        for day in year.days:
            if not day.part1_solved and not day.part2_solved:
                table[day.day].append(None)
                continue

            folder_link = f'{year.year}/{day.folder_name.replace(" ", "%20")}'

            if day.readme_exists:
                stars = 2 if day.day == 25 and day.part1_solved else day.part1_solved + day.part2_solved
                table[day.day].append((html_link('💎' * stars, folder_link), {'align': 'center'}))
                continue

            part_1_link = f'{folder_link}/part1.py'
            part_2_link = f'{folder_link}/part2.py'

            if day.day == 25:
                table[day.day].append(
                    (html_link('⭐' * 2, part_1_link), {'align': 'center'})
                    if day.part1_solved else None
                )

            else:
                text = ''
                if day.part1_solved:
                    text += html_link('⭐', part_1_link)
                if day.part2_solved:
                    text += html_link('⭐', part_2_link)

                if not text:
                    table[day.day].append(None)
                else:
                    table[day.day].append((text, {'align': 'center'}))

    with open(readme_path, 'r', encoding='utf-8') as file:
        readme = file.read()

    readme = re.sub(
        r'(<!-- Main table start -->).+(<!-- Main table end -->)',
        lambda match: match.group(1) + '\n' + table_to_html(table, headers_on=True) + '\n' + match.group(2),
        readme,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(readme)


def gen_year_table(year: Year):
    if not year.solved:
        return
    print(f'Generating README table for year {year.year}...')

    table = [[None, ('Part 1', {'align': 'center'}), ('Part 2', {'align': 'center'})]]

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
