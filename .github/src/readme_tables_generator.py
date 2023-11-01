from bs4 import BeautifulSoup
from itertools import chain
from os.path import isfile
import re

from utils import md_link, html_link, req_get_parallel


REGEX = {
    "solved_table": r"(<!-- Solved table start -->).+(<!-- Solved table end -->)",
    "puzzle_title": r"---\s*Day\s*\d+:\s*(.+?)\s*---"
}


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
        markdown[-1].append(" {:^{}} ".format(
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
            " {:<{}} ".format(
                table[line][column],
                column_sizes[column] + (column != 0 and '⭐' not in table[line][column])  # Asjustment for ⭐ symbol
            )
            for column in range(columns_num)
        ])

    # Build table from lines
    return '\n'.join("|{}|".format('|'.join(line)) for line in markdown)


def gen_global_table(readme_path, solved):
    print("Generating global README table...")
    if not isfile(readme_path):
        return

    table = [[""]] + [["Day {}".format(day + 1)] for day in range(25)]

    for year in solved:
        table[0].append(md_link(year, year))
        for day in range(25):
            day_url_name = "Day%20{:02d}".format(day + 1)

            if solved[year][day][2]:
                # Day has README (both parts solved)
                table[day + 1].append(md_link("⭐⭐", "{}/{}".format(year, day_url_name)))

            elif day + 1 == 25 and solved[year][day][0] and not solved[year][day][1]:
                # This is the 25th day, which can provide both starts for solving the only part
                table[day + 1].append(md_link("⭐⭐", "{}/{}/part1.py".format(year, day_url_name)))

            else:
                table[day + 1].append(
                    (md_link("⭐", "{}/{}/part1.py".format(year, day_url_name)) if solved[year][day][0] else "") +
                    (md_link("⭐", "{}/{}/part2.py".format(year, day_url_name)) if solved[year][day][1] else "")
                )

    with open(readme_path, 'r', encoding="utf-8") as file:
        readme = file.read()

    readme = re.sub(
        REGEX["solved_table"],
        lambda match: match.group(1) + '\n' + table2md(table) + '\n' + match.group(2),
        readme,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(readme_path, 'w', encoding="utf-8") as file:
        file.write(readme)


def html_wrap(content, before, after):
    yield before
    if isinstance(content, str):
        yield '\t' + content
    else:
        for line in content:
            yield '\t' + line
    yield after


def gen_year_table(readme_path, solved, year):
    print("Generating README table for year {}...".format(year))
    if not isfile(readme_path):
        return

    day_pages = req_get_parallel("https://adventofcode.com/{}/day/{}".format(year, day + 1) for day in range(25))

    table = [html_wrap(
        ("<th>" + item + "</th>" for item in ("", "Part 1", "Part 2")),
        "<tr>", "</tr>"
    )]

    for day in range(25):
        day_url_name = "Day%20{:02d}".format(day + 1)

        day_name = "Day {}: {}".format(
            day + 1,
            re.fullmatch(
                REGEX["puzzle_title"],
                BeautifulSoup(day_pages[day].text, "lxml")
                .find("body").find("main").find("article").find("h2").text,
                flags=re.IGNORECASE | re.UNICODE
            ).group(1)
        )

        table.append(html_wrap(
            (
                "<td>" + (
                    html_link(day_name, day_url_name) if solved[day][2] else day_name
                ) + "</td>",

                '<td{} align="center">'.format(' colspan="2"' if day + 1 == 25 and not solved[day][1] else "") + (
                    html_link("⭐⭐", day_url_name + "/part1.py")
                    if solved[day][0] and day + 1 == 25 and not solved[day][1] else
                    html_link("⭐", day_url_name + "/part1.py")
                    if solved[day][0] else
                    ""
                ) + "</td>",

                *(
                    () if day + 1 == 25 and not solved[day][1] else
                    (
                        '<td align="center">' + (
                            html_link("⭐", day_url_name + "/part2.py") if solved[day][1] else ""
                        ) + "</td>",
                    )
                )
            ),
            "<tr>", "</tr>"
        ))

    table = html_wrap(chain(*table), "<table>", "</table>")

    with open(readme_path, 'r', encoding="utf-8") as file:
        readme = file.read()

    readme = re.sub(
        REGEX["solved_table"],
        lambda match: match.group(1) + '\n' + '\n'.join(table) + '\n' + match.group(2),
        readme,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(readme_path, 'w', encoding="utf-8") as file:
        file.write(readme)
