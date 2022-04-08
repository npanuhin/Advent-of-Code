from os.path import isdir, isfile
from sys import argv
import os
import re

from readme_tables_generator import gen_global_table, gen_year_table
from website_generator import gen_home_page, gen_year_page
from replace_tabs import replace_tabs
from readme_exec import readme_exec

from utils import mkpath


ROOT_PATH = "../"


def main(no_debug=True):
    print("Starting...")
    solved = {}

    for year in range(2000, 3000):
        year_path = mkpath(ROOT_PATH, year)
        if not isdir(year_path):
            continue

        #                part1  part1  README
        solved[year] = [[False, False, False] for _ in range(25)]

        # Handle days
        for day in range(0, 25):
            day_path = mkpath(year_path, "Day {:02d}".format(day + 1))
            if not isdir(day_path):
                continue

            files = [filename for filename in os.listdir(day_path) if isfile(mkpath(day_path, filename))]
            solved[year][day] = ["part1.py" in files, "part2.py" in files, "README.md" in files]

            # Long line warning
            for filename in files:
                if os.path.splitext(filename)[1] == ".py":
                    with open(mkpath(day_path, filename), 'r', encoding="utf-8") as file:
                        for line in file:
                            if len(line.strip()) > 120:
                                print("Warning: long line detected in {}".format(mkpath(day_path, filename)))

            # Handle solution files: Replace tabs with spaces
            if no_debug:
                if solved[year][day][0]:
                    replace_tabs(mkpath(day_path, "part1.py"))
                if solved[year][day][1]:
                    replace_tabs(mkpath(day_path, "part2.py"))

            # Handle day README
            if "README.md" not in files:
                continue
            readme_path = mkpath(day_path, "README.md")

            with open(readme_path, 'r', encoding="utf-8") as file:
                readme = file.read()

            # Place non-breaking spaces in markdown `code` tags:
            readme = re.sub(r"`[^`\n\t\b\r]+`", lambda m: m.group(0).replace(' ', chr(0x2007)), readme)

            # Handle "<!-- Execute code: "smth" -->" blocks
            if no_debug:
                readme = readme_exec(readme, day_path)

            with open(readme_path, 'w', encoding="utf-8") as file:
                file.write(readme)

        # Handle year README and webpage
        if no_debug:
            gen_year_table(mkpath(year_path, "README.md"), solved[year], year)
            gen_year_page(mkpath(ROOT_PATH, "docs", year, "index.html"), solved[year], year)

    # Handle global README and webpage
    if no_debug:
        gen_global_table(mkpath(ROOT_PATH, "README.md"), solved)
        gen_home_page(mkpath(ROOT_PATH, "docs", "index.html"), solved)


if __name__ == "__main__":
    main(len(argv) > 1 and argv[1] == "no-debug")
