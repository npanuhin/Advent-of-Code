from sys import argv
import os

# from src.readme_tables_generator import gen_global_table, gen_year_table
# from src.website_generator import gen_home_page, gen_year_page
from src.replace_tabs import replace_tabs
# from src.readme_exec import readme_exec
from src.utils import mkpath


ROOT_PATH = '../'


class Day:
    def __init__(self, year, day):
        self.year = year
        self.day = day

        self.path = mkpath(ROOT_PATH, year, f'Day {(day + 1):02d}')
        self.solved = os.path.isdir(self.path)

        self.part1_path = mkpath(self.path, 'part1.py')
        self.part1_solved = os.path.isfile(self.part1_path)

        self.part2_path = mkpath(self.path, 'part2.py')
        self.part2_solved = os.path.isfile(self.part2_path)

        self.readme_path = mkpath(self.path, 'README.md')
        self.readme_exists = os.path.isfile(self.readme_path)

    def read_readme(self):
        with open(self.readme_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write_readme(self, readme):
        with open(self.readme_path, 'w', encoding='utf-8') as file:
            file.write(readme)


def main(no_debug=True):
    print('Starting...')
    solved: dict[str, list[Day]] = {}

    for year in range(2000, 3000):
        year_path = mkpath(ROOT_PATH, year)
        if not os.path.isdir(year_path):
            continue

        solved[year] = [Day(year, day + 1) for day in range(25)]

        for day in solved[year]:
            if not day.solved:
                continue

            # -------------------------------- Solution files: Replace tabs with spaces --------------------------------
            if no_debug:
                if day.part1_solved:
                    replace_tabs(mkpath(day.path, 'part1.py'))
                if day.part2_solved:
                    replace_tabs(mkpath(day.path, 'part2.py'))

            # ----------------------------------------------- Day README -----------------------------------------------
            if day.readme_exists:
                readme = day.read_readme()

                # Place non-breaking spaces in markdown `code` tags:
                # readme = re.sub(r'`[^`\n\t\b\r]+`', lambda m: m.group(0).replace(' ', chr(0x2007)), readme)

                # Handle '<!-- Execute code: 'smth' -->' blocks
                # if no_debug:
                #     readme = readme_exec(readme, day.path)

                day.write_readme(readme)

            # ------------------------------------ Text files: newlines and the end ------------------------------------
            for filename in os.listdir(day.path):
                filepath = mkpath(day.path, filename)

                if not os.path.isfile(filepath):
                    continue

                if os.path.splitext(filename)[1] in ('.txt', '.py', '.md'):
                    with open(filepath, 'r', encoding='utf-8') as file:
                        file.seek(0, 2)
                        if file.tell() == 0:
                            ends_with_newline = True
                        else:
                            file.seek(file.tell() - 1, 0)
                            ends_with_newline = file.read() == '\n'

                    if not ends_with_newline:
                        with open(filepath, 'a', encoding='utf-8') as file:
                            file.write('\n')

        # # Handle year README and webpage
        # if no_debug:
        #     gen_year_table(mkpath(year_path, 'README.md'), solved[year], year)
        #     gen_year_page(mkpath(ROOT_PATH, 'docs', year, 'index.html'), solved[year], year)

    # # Handle global README and webpage
    # if no_debug:
    #     gen_global_table(mkpath(ROOT_PATH, 'README.md'), solved)
    #     gen_home_page(mkpath(ROOT_PATH, 'docs', 'index.html'), solved)


if __name__ == '__main__':
    main(len(argv) > 1 and argv[1] == 'no-debug')
