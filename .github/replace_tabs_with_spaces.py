import os

ROOT = "../"
EXTENSIONS = (".py", ".md")


def mkpath(*paths):
    return os.path.normpath(os.path.join(*paths))


print("Replacing tabs with spaces...")

for path, folders, files in os.walk(mkpath(ROOT)):
    for filename in files:
        if os.path.splitext(filename)[1] in EXTENSIONS:
            print(mkpath(path, filename))

            with open(mkpath(path, filename), 'r', encoding="utf-8") as file:
                content = file.read()

            with open(mkpath(path, filename), 'w', encoding="utf-8") as file:
                file.write(content.replace('\t', ' ' * 4))
