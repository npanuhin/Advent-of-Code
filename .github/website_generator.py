from bs4 import BeautifulSoup
from os.path import isfile
import re

from utils import mkpath, req_get


YEAR_START = 2015
YEAR_END = max(
    int(event.text.strip()[1:-1])
    for event in BeautifulSoup(req_get("https://adventofcode.com/2015/events").text, "lxml")
    .find("body").find("main").find_all("div", class_="eventlist-event")
)


def gen_home_page(target_path, solved):
    if not isfile(target_path):
        return

    list_items = [
        (
            '<li><a href="{year}">[{year}]</a></li>'
            if year in solved else
            '<li>[{year}]</li>'
        ).format(year=year)
        for year in range(YEAR_START, YEAR_END + 1)
    ]

    with open(target_path, 'r', encoding="utf-8") as file:
        page = file.read()

    page = re.sub(
        r"(\t+)<ul\s+class=\"year_list\">.+?</ul>",
        r'\1<ul class="year_list">{}\n\1</ul>'.format(
            ''.join('\n\t' + r'\1' + str(item) for item in reversed(list_items))
        ),
        page,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(target_path, 'w', encoding="utf-8") as file:
        file.write(page)


def gen_year_page(target_path, solved, year):
    if not isfile(target_path):
        return

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

    with open(target_path, 'r', encoding="utf-8") as file:
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

    with open(target_path, 'w', encoding="utf-8") as file:
        file.write(page)
