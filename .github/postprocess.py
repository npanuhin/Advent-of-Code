from sys import argv
import os

from src.readme_tables_generator import gen_year_table  # , gen_global_table
# from src.website_generator import gen_home_page, gen_year_page
# from src.readme_exec import readme_exec
from src.utils import mkpath
from src.year import Year
from src.day import Day


ROOT_PATH = Day.ROOT_PATH = Year.ROOT_PATH = '../'


def main(no_debug=True):
    print('Starting...')
    solved: dict[int, Year] = {}

    for year_num in range(2000, 3000):
        year = Year(year_num)
        if not year.solved:
            continue

        solved[year] = Year(year)

        for day in year.days:
            if not day.solved:
                continue

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

        # Handle year README and webpage
        gen_year_table(year)
        # if no_debug:
        #     gen_year_table(mkpath(year_path, 'README.md'), solved[year], year)
        #     gen_year_page(mkpath(ROOT_PATH, 'docs', year, 'index.html'), solved[year], year)

    # Handle global README and webpage
    # gen_global_table(mkpath(ROOT_PATH, 'README.md'), solved)
    # if no_debug:
    #     gen_global_table(mkpath(ROOT_PATH, 'README.md'), solved)
    #     gen_home_page(mkpath(ROOT_PATH, 'docs', 'index.html'), solved)


if __name__ == '__main__':
    main(len(argv) > 1 and argv[1] == 'no-debug')
