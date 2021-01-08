import os
import re
import sys
from timeit import timeit


REGEX = {
    "NBS": re.compile(r"`[^`\n\t\b\r]+`"),
    "exec_code": re.compile(
        r"^<!-- Execute code: \"([\w\.]+)\" -->$\s*(?:```(\w*)\s*?[^`]*?```)?\s*(?:```\s*?[^`]*?\s*?```)?\s*(?:#+\s+Execution time:\s*?([^`]+?)?)?$",
        flags=re.MULTILINE
    ),
    "exec_code_replace": "<!-- Execute code: \"{}\" -->\n```{}\n{}\n```\n```\n{}\n```\n###### Execution time: {}"
}


MAX_EXEC_TIME = 30000
MIN_REPEATS = 5
MAX_REPEATS = 100


def mkpath(*paths):
    return os.path.normpath(os.path.join(*paths))


def format_time(seconds):
    if seconds == -1:
        return "None"

    milliseconds = seconds * 1000

    if milliseconds < 1:
        return "< 1ms"

    if milliseconds < 250:
        return str(int(round(milliseconds, 0))) + " ms"

    if milliseconds < 900:
        return "< 1s"

    return str(int(round(milliseconds / 1000, 0))) + " s"


def count_time(code, repeats, stdout=None):
    cur_stdout = sys.stdout
    sys.stdout = stdout
    try:
        exec_time = timeit(code if code else "pass", number=repeats) / repeats
    except Exception:
        exec_time = -1
    sys.stdout = cur_stdout

    return exec_time


def generate_exec_code(path):
    print("Handling \"{}\" file...".format(path))

    folder, filename = os.path.split(path)
    cur_path = os.getcwd()
    os.chdir(folder)

    with open(filename, 'r', encoding="utf-8") as file:
        code = file.read().strip()

    with open("_tmp_exec_result", 'w', encoding="utf-8") as stdout_file:
        repeats = int(MAX_EXEC_TIME / (count_time(code, repeats=1, stdout=stdout_file) * 1000))

    with open("_tmp_exec_result", 'r', encoding="utf-8") as stdout_file:
        exec_result = stdout_file.read().strip()

    os.remove("_tmp_exec_result")

    exec_time = format_time(count_time(code, repeats=max(MIN_REPEATS, min(MAX_REPEATS, repeats))))

    os.chdir(cur_path)
    return code, exec_result, exec_time


def main(root_path):
    for path, folders, files in os.walk(root_path):
        if "README.md" in files:
            readme_path = mkpath(path, "README.md")

            with open(readme_path, 'r', encoding="utf-8") as file:
                readme = file.read()

            # Non-breaking space:
            readme = re.sub(REGEX["NBS"], lambda m: m.group(0).replace(" ", " "), readme)
            #                                                                ^ This is non-breaking space

            readme = re.sub(
                REGEX["exec_code"],
                lambda match: REGEX["exec_code_replace"].format(
                    match.group(1),
                    "python" if match.group(2) is None else match.group(2),
                    *generate_exec_code(mkpath(path, match.group(1).strip()))
                ),
                readme
            )

            with open(readme_path, 'w', encoding="utf-8") as file:
                file.write(readme)


if __name__ == "__main__":
    main("../")
