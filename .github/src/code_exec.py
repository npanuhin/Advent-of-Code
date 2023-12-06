from timeit import timeit
from io import StringIO
import sys
import os


from utils import clamp


MAX_EXEC_TIME = 3000  # 3 sec
REPEATS_MIN = 3
REPEATS_MAX = 100


def exec_file(path: str = "", repeats: int = 1) -> tuple[int, str]:
    print(f'Running "{path}...')
    folder, filename = os.path.split(path)
    if not folder:
        folder = '.'

    cur_path = os.getcwd()
    os.chdir(folder)

    with open(filename, encoding='utf-8') as file:
        code = file.read().strip()

    cur_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        exec_time = timeit(code, number=repeats) / repeats
    finally:
        stdout, sys.stdout = sys.stdout, cur_stdout
        os.chdir(cur_path)

    return exec_time * 1000, stdout.getvalue().strip()


def count_time(path: str) -> tuple[int, str]:
    print(f'Running "{path}...')

    single_time, output = exec_file(path)[0]

    repeats = MAX_EXEC_TIME // single_time
    exec_time = exec_file(path, repeats=clamp(repeats, REPEATS_MIN, REPEATS_MAX))[0]

    return exec_time, output


if __name__ == '__main__':
    with open('tmp.py', 'w', encoding='utf-8') as file:
        file.write('print("Hello, world!")')

    print(exec_file('tmp.py'))

    os.remove('tmp.py')
