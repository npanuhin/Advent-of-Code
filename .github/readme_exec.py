from timeit import timeit
from io import StringIO
from math import ceil
import sys
import os
import re

from utils import mkpath, clamp


REGEX = {
    "exec_code": re.compile(
        (
            r"^<!-- Execute code: \"([\w\-\.]+)\" -->$(?:\s*```(\w+?)\s.*?```)?"
            r"(?:\s*```.*?```)?\s*(?:^#+\s+Execution time:\s*(.+?)?)?$"
        ),
        flags=re.MULTILINE | re.UNICODE | re.DOTALL
    ),
    "exec_code_replace": "<!-- Execute code: \"{}\" -->\n```{}\n{}\n```\n```\n{}\n```\n###### Execution time: {}"
}

MAX_EXEC_TIME = 10000
REPEATS_CLAMP = (3, 30)


def format_time(milliseconds):
    if milliseconds is None:
        return "None"

    if milliseconds < 1:
        return "< 1ms"

    if milliseconds < 250:
        return "{}ms".format(round(milliseconds))

    if milliseconds < 950:
        return "< 1s"

    return "{}s".format(round(milliseconds / 1000))


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

    if not match1.group(1) and not match2.group(1) and match1.group(3) == match2.group(3) and \
            abs(int(match1.group(2)) - int(match2.group(2))) <= ceil(max(
                abs(int(match1.group(2))),
                abs(int(match2.group(2)))
            ) / 10):
        return False

    return True


def count_time(code, repeats=1, stdout=None):
    cur_stdout = sys.stdout
    sys.stdout = stdout
    try:
        exec_time = timeit(code if code else "pass", number=repeats) / repeats
    except Exception as e:
        print(e, sys.stdout, file=cur_stdout)
        exec_time = None
    sys.stdout = cur_stdout

    return exec_time * 1000


def exec_code(path):
    print("Handling \"{}\"...".format(path))
    folder, filename = os.path.split(path)

    cur_path = os.getcwd()
    os.chdir(folder)

    with open(filename, 'r', encoding="utf-8") as file:
        code = file.read().strip()

    stdout = StringIO()

    repeats = int(MAX_EXEC_TIME / count_time(code, stdout=stdout))

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


def readme_exec(text, path):
    return re.sub(
        REGEX["exec_code"],
        lambda match: handle_match(mkpath(path, match.group(1)), match),
        text
    )
