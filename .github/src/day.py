import os

from src.utils import mkpath


class Day:
    ROOT_PATH = "."

    def __init__(self, year, day):
        self.year = year
        self.day = day

        self.path = mkpath(Day.ROOT_PATH, year, f'Day {day:02d}')
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
