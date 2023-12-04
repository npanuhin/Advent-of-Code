import os

from src.readme_tables_generator import gen_year_table, gen_global_table
from src.website_generator import gen_global_page, gen_year_page
from src.code_exec import exec_code
from src.utils import mkpath
from src.year import Year
from src.day import Day


ROOT_PATH = Day.ROOT_PATH = Year.ROOT_PATH = '../'


def main():
    print('Starting...')
    solved: dict[int, Year] = {}

    for year_num in range(2000, 3000):
        year = Year(year_num)
        if not year.solved:
            continue

        solved[year_num] = year

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

            # ------------------------------------------ Dual solution check -------------------------------------------
            if day.dual_solution_exists:
                part1_output = exec_code(day.part1_path)[1]
                part2_output = exec_code(day.part2_path)[1]
                dual_output = exec_code(day.dual_solution_path)[1]

                combined_outputs = (part1_output + '\n' + part2_output).strip()

                assert dual_output == combined_outputs, (
                    f'Dual solution output mismatch!\n'
                    f'Part 1 output:\n{part1_output}\n'
                    f'Part 2 output:\n{part2_output}\n'
                    f'Dual solution output:\n{dual_output}'
                )

        # Handle year README and webpage
        gen_year_table(year)
        gen_year_page(year, mkpath(ROOT_PATH, 'docs', year.year, 'index.html'))

    # Handle global README and webpage
    gen_global_table(solved, mkpath(ROOT_PATH, 'README.md'))
    gen_global_page(solved, mkpath(ROOT_PATH, 'docs', 'index.html'))


if __name__ == '__main__':
    main()
