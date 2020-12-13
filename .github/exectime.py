from timeit import timeit
import sys
import os
import re

repeats = 20


def mkpath(*paths):
    return os.path.normpath(os.path.join(*paths))


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


def format_time(ms_time):
    if ms_time < 1:
        return "< 1ms"

    if ms_time < 300:
        return str(int(round(ms_time, 0))) + " ms"

    if ms_time < 1000:
        return "< " + str(int(round(ms_time / 1000, 0))) + "s"

    return str(int(round(ms_time / 1000, 0))) + " s"


def count_day(root_path, day):
    day_path = mkpath(root_path, "2020", "Day {}".format(str(day).zfill(2)))

    if os.path.isdir(day_path):

        print("Day {}:".format(day))

        part1_path = mkpath(day_path, "part1.py")
        part2_path = mkpath(day_path, "part2.py")

        part1_exec_time = format_time(count_time(part1_path, repeats) * 1000)
        part2_exec_time = format_time(count_time(part2_path, repeats) * 1000)

        print("   part1: {}".format(part1_exec_time))
        print("   part2: {}\n".format(part2_exec_time))

        if os.path.isfile(mkpath(day_path, "README.md")):

            with open(mkpath(day_path, "README.md"), 'r', encoding="utf-8") as file:
                text = file.read()

            text = re.sub(r"(## Part 1(.|\n)+###### Execution time:)\s*<?\s*[\d\.]+.+$", r"\1 " + part1_exec_time, text, re.U)
            text = re.sub(r"(## Part 2(.|\n)+###### Execution time:)\s*<?\s*[\d\.]+.+$", r"\1 " + part2_exec_time, text, re.U)

            with open(mkpath(day_path, "README.md"), 'w', encoding="utf-8") as file:
                file.write(text)


def main(root_path, repeats):
    for day in range(1, 25):
        count_day(root_path, day)


if __name__ == "__main__":
    main("../", repeats)
