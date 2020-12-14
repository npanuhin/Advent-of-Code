import os
from re import sub as re_sub


def mkpath(*paths):
    return os.path.normpath(os.path.join(*paths))

def non_breaking_space(root_path):

    for path, folders, files in os.walk(root_path):
        if "README.md" in files:
            readme_path = mkpath(path, "README.md")

            with open(readme_path, 'r', encoding="utf-8") as file:
                readme = file.read()

            readme = re_sub(r"`[^`\n\t\b\r]+`", lambda m: m.group(0).replace(" ", " "), readme)
            #                                                                      ^ This is non-breaking space

            with open(readme_path, 'w', encoding="utf-8") as file:
                file.write(readme)


def main(root_path):
    non_breaking_space(root_path)


if __name__ == "__main__":
    main("../")
