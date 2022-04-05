from os.path import isdir, isfile
import os
import re

from readme_tables_generator import gen_global_table, gen_year_table
# from website_generator import gen_home_page, gen_year_page
from readme_exec import readme_exec
from utils import mkpath


ROOT_PATH = "../"

REGEX = {
    "markdown_code": r"`[^`\n\t\b\r]+`"
}


def main():
    print("Starting...")
    solved = {}

    for year in range(2000, 3000):
        year_path = mkpath(ROOT_PATH, year)
        if not isdir(year_path):
            continue

        solved[year] = [[False, False] for _ in range(25)]

        # Handle days
        for day in range(0, 25):
            day_path = mkpath(year_path, "Day {:02d}".format(day + 1))
            if not isdir(day_path):
                continue

            files = [filename for filename in os.listdir(day_path) if isfile(mkpath(day_path, filename))]
            solved[year][day] = ["part1.py" in files, "part2.py" in files]

            # Long line warning
            for filename in files:
                if os.path.splitext(filename)[1] == ".py":
                    with open(mkpath(day_path, filename), 'r', encoding="utf-8") as file:
                        for line in file:
                            if len(line.strip()) > 120:
                                print("Warning: long line detected in {}".format(mkpath(day_path, filename)))

            # Handle day README
            if "README.md" not in files:
                continue
            readme_path = mkpath(day_path, "README.md")

            with open(readme_path, 'r', encoding="utf-8") as file:
                readme = file.read()

            # Place non-breaking spaces in markdown `code` tags:
            readme = re.sub(REGEX["markdown_code"], lambda m: m.group(0).replace(' ', chr(0x2007)), readme)

            # Handle "<!-- Execute code: "smth" -->" blocks
            readme = readme_exec(readme, day_path)

            with open(readme_path, 'w', encoding="utf-8") as file:
                file.write(readme)

        # Handle year README
        gen_year_table(year_path, solved[year], year)

    # Handle global README
    gen_global_table(ROOT_PATH, solved)


if __name__ == "__main__":
    main()
