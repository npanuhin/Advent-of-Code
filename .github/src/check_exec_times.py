from sys import path as sys_path
import os

sys_path.append("../")

from readme_exec import count_time
from utils import mkpath


ROOT_PATH = "../../"


for year in range(2000, 3000):
    for path, folders, files in os.walk(mkpath(ROOT_PATH, year)):
        cur_path = os.getcwd()
        os.chdir(path)

        for filename in files:
            if os.path.splitext(filename)[1] != ".py":
                continue

            with open(filename, 'r', encoding="utf-8") as file:
                code = file.read().strip()

            print(mkpath(path, filename), str(round(count_time(code))) + "ms")

        os.chdir(cur_path)

# path = "../../2020/Day 23/"
# filename = "part2.py"

# cur_path = os.getcwd()
# os.chdir(path)

# with open(filename, 'r', encoding="utf-8") as file:
#     code = file.read().strip()

# print(mkpath(path, filename), str(round(count_time(code))) + "ms")

# os.chdir(cur_path)
