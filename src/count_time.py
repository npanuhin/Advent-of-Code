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


def main(repeats):
    for day in range(1, 25):
        day = str(day).zfill(2)

        print("Day {}:".format(day))

        if os.path.isdir("../2020/Day {}".format(day)):

            part1_path = "../2020/Day {}/part1.py".format(day)
            part2_path = "../2020/Day {}/part2.py".format(day)

            print("   part1: {}".format(
                round(count_time(part1_path, repeats) * 1000, 1)
            ))

            print("   part2: {}\n".format(
                round(count_time(part2_path, repeats) * 1000, 2)
            ))


if __name__ == "__main__":
    main(repeats)
