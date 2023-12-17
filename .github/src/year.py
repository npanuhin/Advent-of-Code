import os

from utils import mkpath
from day import Day


class Year:
    def __init__(self, year_num: int):
        self.year = year_num

        self.path = mkpath(os.path.dirname(__file__), '../../', year_num)
        self.solved = os.path.isdir(self.path)

        self.readme_path = mkpath(self.path, 'README.md')

        if not self.solved:
            self.days = []
            self.readme_exists = False
        else:
            self.days = [Day(year_num, day + 1) for day in range(25)]
            self.readme_exists = os.path.isfile(self.readme_path)

    def read_readme(self):
        with open(self.readme_path, encoding='utf-8') as file:
            return file.read()

    def write_readme(self, readme: str):
        with open(self.readme_path, 'w', encoding='utf-8') as file:
            file.write(readme)

    def __repr__(self):
        return f'Year({self.year}, solved={self.solved}, readme_exists={self.readme_exists})'
