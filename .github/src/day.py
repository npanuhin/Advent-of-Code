import os

from utils import mkpath


class Day:
    def __init__(self, year_num: int, day_num: int):
        self.year = year_num
        self.day = day_num

        self.folder_name = f'Day {day_num:02d}'
        self.url_name = self.folder_name.replace(' ', '%20')

        self.path = mkpath(os.path.dirname(__file__), '../../', year_num, self.folder_name)
        self.solved = os.path.isdir(self.path)

        self.part1_path = mkpath(self.path, 'part1.py')
        self.part1_solved = os.path.isfile(self.part1_path)

        self.part2_path = mkpath(self.path, 'part2.py')
        self.part2_solved = os.path.isfile(self.part2_path)

        self.readme_path = mkpath(self.path, 'README.md')
        self.readme_exists = os.path.isfile(self.readme_path)

        self.dual_solution_path = mkpath(self.path, 'solution.py')
        self.dual_solution_exists = os.path.isfile(self.dual_solution_path)

    def read_readme(self):
        with open(self.readme_path, encoding='utf-8') as file:
            return file.read()

    def write_readme(self, readme: str):
        with open(self.readme_path, 'w', encoding='utf-8') as file:
            file.write(readme)

    def __repr__(self):
        return (
            f'Day({self.year}, {self.day}, solved={self.solved}, readme_exists={self.readme_exists}, '
            f'part_1_solved={self.part1_solved}, part_2_solved={self.part2_solved})'
        )
