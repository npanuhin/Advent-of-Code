def replace_tabs(path):
    with open(path, 'r', encoding="utf-8") as file:
        content = file.read()

    with open(path, 'w', encoding="utf-8") as file:
        file.write(content.replace('\t', ' ' * 4))


def main():
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
                replace_tabs(mkpath(path, filename))


if __name__ == "__main__":
    main()
