import os

from src.utils import mkpath
from src.day import Day


class Year:
    ROOT_PATH = "."

    def __init__(self, year):
        self.year = year

        self.path = mkpath(Year.ROOT_PATH, year)
        self.solved = os.path.isdir(self.path)

        self.days = [Day(year, day + 1) for day in range(25)]

        self.readme_path = mkpath(self.path, 'README.md')
        self.readme_exists = os.path.isfile(self.readme_path)

    def read_readme(self):
        with open(self.readme_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write_readme(self, readme):
        with open(self.readme_path, 'w', encoding='utf-8') as file:
            file.write(readme)
