from os import walk as os_walk
from os.path import splitext

from utils import mkpath


ROOT = "../"
EXTENSIONS = (".py", ".md")


print("Replacing tabs with spaces...")

for path, folders, files in os_walk(mkpath(ROOT)):
    for filename in files:
        if splitext(filename)[1] in EXTENSIONS:
            print(mkpath(path, filename))

            with open(mkpath(path, filename), 'r', encoding="utf-8") as file:
                content = file.read()

            with open(mkpath(path, filename), 'w', encoding="utf-8") as file:
                file.write(content.replace('\t', ' ' * 4))
