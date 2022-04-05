from bs4 import BeautifulSoup
from os.path import isfile
import re

from utils import mkpath, md_link, req_get_parallel


REGEX = {
    "solved_table": r"(<!-- Solved table start -->).+(<!-- Solved table end -->)",
    "puzzle_title": r"---\s*Day\s*\d+:\s*(.+?)\s*---"
}


def gen_global_table(root_path, solved):
    print("Generating global README table...")
    readme_path = mkpath(root_path, "README.md")
    if not isfile(readme_path):
        return

    table = [[""]] + [["Day {}".format(day + 1)] for day in range(25)]
    columns_num = len(solved) + 1

    for year in solved:
        table[0].append(md_link(year, "./{}".format(year)))
        for day in range(25):
            read_day = day + 1
            day_path_name = "Day {:02d}".format(read_day)
            day_url_name = day_path_name.replace(' ', "%20")
            day_path = mkpath(root_path, year, day_path_name)

            if isfile(mkpath(day_path, "README.md")):
                # Day has README (both parts solved)
                table[read_day].append(md_link("⭐⭐", "./{}/{}".format(year, day_url_name)))

            elif read_day == 25 and solved[year][day][0] and not solved[year][day][1]:
                # This is the 25th day, which can provide both starts for solving the only part
                table[read_day].append(md_link("⭐⭐", "./{}/{}/part1.py".format(year, day_url_name)))

            else:
                table[read_day].append(
                    (md_link("⭐", "./{}/{}/part1.py".format(year, day_url_name)) if solved[year][day][0] else "") +
                    (md_link("⭐", "./{}/{}/part2.py".format(year, day_url_name)) if solved[year][day][1] else "")
                )

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
    markdown = '\n'.join("|{}|".format('|'.join(line)) for line in markdown)

    with open(readme_path, 'r', encoding="utf-8") as file:
        readme = file.read()

    readme = re.sub(
        REGEX["solved_table"],
        lambda match: match.group(1) + '\n' + markdown + '\n' + match.group(2),
        readme,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(readme_path, 'w', encoding="utf-8") as file:
        file.write(readme)


def gen_year_table(year_path, solved, year):
    print("Generating README table for year {}...".format(year))
    readme_path = mkpath(year_path, "README.md")
    if not isfile(readme_path):
        return

    table = [["", "Part 1", "Part 2"]]

    day_pages = req_get_parallel("https://adventofcode.com/{}/day/{}".format(year, day + 1) for day in range(25))

    for day in range(25):
        real_day = day + 1
        day_path_name = "Day {:02d}".format(real_day)
        day_url_name = day_path_name.replace(' ', "%20")
        day_path = mkpath(year_path, day_path_name)

        puzzle_title = re.fullmatch(
            REGEX["puzzle_title"],
            BeautifulSoup(day_pages[day].text, "lxml")
            .find("body").find("main").find("article").find("h2").text,
            flags=re.IGNORECASE | re.UNICODE
        ).group(1)

        day_name = "Day {}: {}".format(real_day, puzzle_title)

        table.append([
            md_link(day_name, "./" + day_url_name) if isfile(mkpath(day_path, "README.md")) else " " + day_name,

            md_link("⭐", "./" + day_url_name + "/part1.py") if solved[day][0] else "",

            md_link("⭐", "./" + day_url_name + "/part2.py") if real_day == 25 and solved[day][0]
            else md_link("⭐", "./" + day_url_name + "/part2.py") if solved[day][1]
            else ""
        ])

    markdown = [[]]

    # Precalculate table column sizes
    column_sizes = [
        max(len(line[column]) for line in table)
        for column in range(3)
    ]

    # Header
    for column in range(3):
        markdown[-1].append(" {:^{}} ".format(
            table[0][column],
            column_sizes[column] + (column == 1 and '⭐' not in table[0][column])  # Asjustment for ⭐ symbol
        ))

    # Header separator
    markdown.append([
        ':' + '-' * (column_size + {0: 2, 1: 1, 2: 0}[column]) + ':'
        for column, column_size in enumerate(column_sizes)
    ])
    markdown[-1][0] = markdown[-1][0].strip(':')

    # Table content
    for line in range(1, len(table)):
        markdown.append([
            " {:<{}} ".format(
                table[line][column],
                column_sizes[column] + (column == 1 and '⭐' not in table[line][column])  # Asjustment for ⭐ symbol
            )
            for column in range(3)
        ])

    # Build table from lines
    markdown = '\n'.join("|{}|".format('|'.join(line)) for line in markdown)

    with open(readme_path, 'r', encoding="utf-8") as file:
        readme = file.read()

    readme = re.sub(
        REGEX["solved_table"],
        lambda match: match.group(1) + '\n' + markdown + '\n' + match.group(2),
        readme,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(readme_path, 'w', encoding="utf-8") as file:
        file.write(readme)
