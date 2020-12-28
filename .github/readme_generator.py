import os
import re


REGEX = {
    "NBS": re.compile(r"`[^`\n\t\b\r]+`"),
    "part1_code": re.compile(r"(#+\s+Part 1(?:.|\s)+?```\w*((?:[^`])*?)```\s+```[\s\d]+?```\s+#+\s+Execution time):?.*?$", flags=re.MULTILINE),
    "part2_code": re.compile(r"(#+\s+Part 2(?:.|\s)+?```\w*((?:[^`])*?)```\s+```[\s\d]+?```\s+#+\s+Execution time):?.*?$", flags=re.MULTILINE)
}


def mkpath(*paths):
    return os.path.normpath(os.path.join(*paths))


def non_breaking_space(root_path):
    for path, folders, files in os.walk(root_path):
        if "README.md" in files:
            readme_path = mkpath(path, "README.md")

            with open(readme_path, 'r', encoding="utf-8") as file:
                readme = file.read()

            readme = re.sub(REGEX["NBS"], lambda m: m.group(0).replace(" ", " "), readme)
            #                                                                      ^ This is non-breaking space

            with open(readme_path, 'w', encoding="utf-8") as file:
                file.write(readme)


def code_paste(root_path):
    for path, folders, files in os.walk(root_path):
        if "README.md" in files:
            readme_path = mkpath(path, "README.md")

            with open(readme_path, 'r', encoding="utf-8") as file:
                readme = file.read()

            if "part1.py" in files:
                with open(mkpath(path, "part1.py"), 'r', encoding="utf-8") as part1_code_file:
                    part1_code = "\n" + part1_code_file.read().strip() + "\n"

                readme = re.sub(REGEX["part1_code"], lambda m: m.group(0).replace(m.group(2), part1_code), readme, count=1)

            if "part2.py" in files:
                with open(mkpath(path, "part2.py"), 'r', encoding="utf-8") as part2_code_file:
                    part2_code = "\n" + part2_code_file.read().strip() + "\n"

                readme = re.sub(REGEX["part2_code"], lambda m: m.group(0).replace(m.group(2), part2_code), readme, count=1)

            with open(readme_path, 'w', encoding="utf-8") as file:
                file.write(readme)


def main(root_path):
    non_breaking_space(root_path)
    code_paste(root_path)


if __name__ == "__main__":
    main("../")
