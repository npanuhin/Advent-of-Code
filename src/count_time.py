from timeit import timeit
import sys
import os

repeats = 100


def count_time(exec_path, repeats):
    exec_time = None

    cur_directory = os.getcwd()

    directory, filename = os.path.split(exec_path)
    os.chdir(directory)

    with open(filename, 'r', encoding="utf-8") as file:
        code = file.read()

    cur_stdout = sys.stdout
    sys.stdout = None
    exec_time = timeit(code if code else "pass", number=repeats) / repeats
    sys.stdout = cur_stdout

    os.chdir(cur_directory)

    return exec_time


def count_day(day):
    day_path = "../2020/Day {}".format(str(day).zfill(2))

    if os.path.isdir(day_path):

        print("Day {}:".format(day))

        part1_path = day_path + "/part1.py"
        part2_path = day_path + "/part2.py"

        print("   part1: {} ms".format(
            round(count_time(part1_path, repeats) * 1000, 2)
        ))

        print("   part2: {} ms\n".format(
            round(count_time(part2_path, repeats) * 1000, 2)
        ))


def main(repeats):
    for day in range(1, 25):
        count_day(day)


if __name__ == "__main__":
    # main(repeats)

    count_day(12)
