from os.path import isdir, isfile
import os
import re

from readme_tables_generator import gen_global, gen_year
from readme_exec import readme_exec
from utils import mkpath


ROOT_PATH = "../"

REGEX = {
    "markdown_code": r"`[^`\n\t\b\r]+`"
}


def main():
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

            if isfile(mkpath(day_path, "part1.py")):
                solved[year][day][0] = True
            if isfile(mkpath(day_path, "part2.py")):
                solved[year][day][1] = True

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
            readme = re.sub(REGEX["markdown_code"], lambda m: m.group(0).replace(" ", " "), readme)

            readme = readme_exec(readme, day_path)

            with open(readme_path, 'w', encoding="utf-8") as file:
                file.write(readme)

        # Handle year README
        gen_year(year_path, solved, year)

    # Handle global README
    gen_global(ROOT_PATH, solved)


if __name__ == "__main__":
    main()
