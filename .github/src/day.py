import os

from src.utils import mkpath


class Day:
    ROOT_PATH = "."

    def __init__(self, year_num, day_num):
        self.year = year_num
        self.day = day_num

        self.folder_name = f'Day {day_num:02d}'
        self.url_name = self.folder_name.replace(' ', '%20')

        self.path = mkpath(Day.ROOT_PATH, year_num, self.folder_name)
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

    def __repr__(self):
        return (
            f'Day({self.year}, {self.day}, solved={self.solved}, readme_exists={self.readme_exists}, '
            f'part_1_solved={self.part1_solved}, part_2_solved={self.part2_solved})'
        )
