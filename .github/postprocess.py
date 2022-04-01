from timeit import timeit
from io import StringIO
import sys
import os
import re


ROOT_PATH = "../"

REGEX = {
    "markdown_code": r"`[^`\n\t\b\r]+`",
    "exec_code": re.compile(
        (
            r"^<!-- Execute code: \"([\w\-\.]+)\" -->$(?:\s*```(\w+?)\s.*?```)?"
            r"(?:\s*```.*?```)?\s*(?:^#+\s+Execution time:\s*(.+?)?)?$"
        ),
        flags=re.MULTILINE | re.UNICODE | re.DOTALL
    ),
    "exec_code_replace": "<!-- Execute code: \"{}\" -->\n```{}\n{}\n```\n```\n{}\n```\n###### Execution time: {}"
}

MAX_EXEC_TIME = 30000 / 1000
REPEATS_CLAMP = (5, 100)


def clamp(x, b, t):
    return b if x < b else t if x > t else x


def mkpath(*paths):
    return os.path.normpath(os.path.join(*paths))


def format_time(seconds):
    if seconds is None:
        return "None"

    milliseconds = seconds * 1000

    if milliseconds < 1:
        return "< 1ms"

    if milliseconds < 250:
        return "{}ms".format(round(milliseconds))

    if milliseconds < 950:
        return "< 1s"

    return "{}s".format(round(seconds))


def need_time_change(old_time, new_time):
    if not old_time:
        return False

    if old_time == "< 1ms" and new_time == "1ms":
        return False

    if old_time == "< 1s" and new_time == "1s":
        return False

    match1 = re.fullmatch(r"(<\s+)?(\d+)(m?s)", old_time, re.IGNORECASE)
    match2 = re.fullmatch(r"(<\s+)?(\d+)(m?s)", new_time, re.IGNORECASE)

    if not match1:
        return True

    if not match2:
        exit("Regex is broken")

    if not match1.group(1) and not match2.group(1) and match1.group(3) == match2.group(3) and \
            abs(int(match1.group(2)) - int(match2.group(2))) <= 1:
        return False

    return True


def count_time(code, repeats, stdout=None):
    cur_stdout = sys.stdout
    sys.stdout = stdout
    try:
        exec_time = timeit(code if code else "pass", number=repeats) / repeats
    except Exception as e:
        print(e, sys.stdout, file=cur_stdout)
        exec_time = None
    sys.stdout = cur_stdout

    return exec_time


def exec_code(path):
    print("Handling \"{}\"...".format(path))
    folder, filename = os.path.split(path)

    cur_path = os.getcwd()
    os.chdir(folder)

    with open(filename, 'r', encoding="utf-8") as file:
        code = file.read().strip()

    stdout = StringIO()

    repeats = int(MAX_EXEC_TIME / count_time(code, repeats=1, stdout=stdout))

    exec_time = count_time(code, repeats=clamp(repeats, *REPEATS_CLAMP))

    os.chdir(cur_path)
    return code, stdout.getvalue().strip(), format_time(exec_time)


def handle_match(path, match):
    code, output, exec_time = exec_code(path)

    return REGEX["exec_code_replace"].format(
        match.group(1),
        "python" if match.group(2) is None else match.group(2),
        code, output,
        exec_time if need_time_change(match.group(3), exec_time) else match.group(3)
    )


def main(root_path):
    for path, folders, files in os.walk(root_path):
        for filename in files:
            if os.path.splitext(filename)[1] == ".py":
                with open(mkpath(path, filename), 'r', encoding="utf-8") as file:
                    for line in file:
                        if len(line.strip()) > 120:
                            print("Warning: long line detected in {}".format(mkpath(path, filename)))

        # continue

        if "README.md" not in files:
            continue

        readme_path = mkpath(path, "README.md")

        with open(readme_path, 'r', encoding="utf-8") as file:
            readme = file.read()

        # Place non-breaking spaces in markdown `code` tags:
        readme = re.sub(REGEX["markdown_code"], lambda m: m.group(0).replace(" ", " "), readme)

        # Execution time
        readme = re.sub(
            REGEX["exec_code"],
            lambda match: handle_match(mkpath(path, match.group(1)), match),
            readme
        )

        with open(readme_path, 'w', encoding="utf-8") as file:
            file.write(readme)


if __name__ == "__main__":
    main(ROOT_PATH)
