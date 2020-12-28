from timeit import timeit
import sys
import os
import re


MAX_EXEC_TIME = 30000
MIN_REPEATS = 5
MAX_REPEATS = 100


def mkpath(*paths):
    return os.path.normpath(os.path.join(*paths))


def count_time(exec_path, repeats):
    cur_directory = os.getcwd()

    directory, filename = os.path.split(exec_path)
    os.chdir(directory)

    with open(filename, 'r', encoding="utf-8") as file:
        code = file.read()

    cur_stdout = sys.stdout
    sys.stdout = None
    try:
        exec_time = timeit(code if code else "pass", number=repeats) / repeats
    except Exception:
        exec_time = -1
    sys.stdout = cur_stdout

    os.chdir(cur_directory)

    return exec_time


def format_time(seconds):
    if seconds == -1:
        return str("Exception")

    milliseconds = seconds * 1000

    if milliseconds < 1:
        return "< 1ms"

    if milliseconds < 300:
        return str(int(round(milliseconds, 0))) + " ms"

    if milliseconds < 1000:
        return "< 1s"

    return str(int(round(milliseconds / 1000, 0))) + " s"


def count_day(root_path, day):
    day_path = mkpath(root_path, "2020", "Day {}".format(str(day).zfill(2)))

    if os.path.isdir(day_path):

        print("Execution time for Day {}:".format(day))

        print(" -> part1: ", end="")
        part1_path = mkpath(day_path, "part1.py")

        repeats = int(MAX_EXEC_TIME / (count_time(part1_path, repeats=1) * 1000))

        part1_exec_time = format_time(count_time(part1_path, repeats=max(MIN_REPEATS, min(MAX_REPEATS, repeats))))
        print(part1_exec_time)

        print(" -> part2: ", end="")
        part2_path = mkpath(day_path, "part2.py")

        repeats = int(MAX_EXEC_TIME / (count_time(part2_path, repeats=1) * 1000))

        part2_exec_time = format_time(count_time(part2_path, repeats=max(MIN_REPEATS, min(MAX_REPEATS, repeats))))
        print(part2_exec_time)

        if os.path.isfile(mkpath(day_path, "README.md")):

            with open(mkpath(day_path, "README.md"), 'r', encoding="utf-8") as file:
                text = file.read()

            text = re.sub(r"(#+ Part 1(?:.|\n)+?#+ Execution time):?.*?$", r"\1: " + part1_exec_time, text, count=1, flags=re.MULTILINE)
            text = re.sub(r"(#+ Part 2(?:.|\n)+?#+ Execution time):?.*?$", r"\1: " + part2_exec_time, text, count=1, flags=re.MULTILINE)

            with open(mkpath(day_path, "README.md"), 'w', encoding="utf-8") as file:
                file.write(text)

        print()


def main(root_path):
    for day in range(1, 25):
        count_day(root_path, day)


if __name__ == "__main__":
    main("../")

    # count_day("../", 11)
