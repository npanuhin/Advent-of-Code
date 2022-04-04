# from markdownTable import markdownTable
import os
import re

# from readme_exec import readme_exec


ROOT_PATH = "../"

REGEX = {
    "markdown_code": r"`[^`\n\t\b\r]+`",
    "global_table": r"(<!-- Global table start -->).+(<!-- Global table end -->)"
}


def mkpath(*paths):
    return os.path.normpath(os.path.join(*map(str, paths)))


def md_link(text, link):
    return "[{}]({})".format(text, link)


def global_readme_table(solved):
    with open(mkpath(ROOT_PATH, "README.md"), 'r', encoding="utf-8") as file:
        readme = file.read()

    table = [[""]] + [["Day {}".format(day)] for day in range(1, 26)]

    for year in solved:
        table[0].append(md_link(year, "./{}".format(year)))
        for day in range(1, 26):
            day_path_name = "Day {:02d}".format(day)
            day_url_name = day_path_name.replace(' ', "%20")
            day_path = mkpath(ROOT_PATH, year, day_path_name)

            if os.path.isfile(mkpath(day_path, "README.md")):
                # Day has README (both parts solved)
                table[day].append(md_link("⭐⭐", "./{}/{}".format(year, day_url_name)))

            elif day == 25 and \
                    os.path.isfile(mkpath(day_path, "part1.py")) and \
                    not os.path.isfile(mkpath(day_path, "part2.py")):
                # This is the 25th day, which can provide both starts for solving one part
                table[day].append(md_link("⭐⭐", "./{}/{}/part1.py".format(year, day_url_name)))

            else:
                table[day].append(
                    (md_link("⭐", "./{}/{}/part1.py".format(year, day_url_name)) if solved[year][day - 1][0] else "") +
                    (md_link("⭐", "./{}/{}/part2.py".format(year, day_url_name)) if solved[year][day - 1][1] else "")
                )

    markdown = [[]]

    # Precalculate table column sizes
    column_sizes = [0] * len(table[0])
    for column in range(len(table[0])):
        for line in table:
            column_sizes[column] = max(column_sizes[column], len(line[column]))

    # Header
    for column in range(len(table[0])):
        column_size = column_sizes[column]
        if column != 0 and '⭐' not in table[0][column]:
            column_size += 1  # Asjustment for ⭐ symbol

        markdown[-1].append(" {:^{}} ".format(table[0][column], column_size))

    # Header separator
    markdown.append([
        ':' + '-' * (column_size + (2 if column == 0 else 1)) + ':'
        for column, column_size in enumerate(column_sizes)
    ])
    markdown[-1][0] = markdown[-1][0].strip(':')

    # Table content
    for line in range(1, len(table)):
        markdown.append([])
        for column in range(len(table[0])):

            # Asjustment for ⭐ symbol
            column_size = column_sizes[column] + (column != 0 and '⭐' not in table[line][column])

            markdown[-1].append(" {:<{}} ".format(table[line][column], column_size))

    # Build table from lines
    markdown = '\n'.join("|{}|".format('|'.join(line)) for line in markdown)

    readme = re.sub(
        REGEX["global_table"],
        lambda match: match.group(1) + '\n' + markdown + '\n' + match.group(2),
        readme,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(mkpath(ROOT_PATH, "README.md"), 'w', encoding="utf-8") as file:
        file.write(readme)


def main():
    solved = {}

    for year in range(2000, 3000):
        year_path = mkpath(mkpath(ROOT_PATH, year))
        if not os.path.isdir(year_path):
            continue

        solved[year] = [[False, False] for _ in range(25)]

        # Handle days
        for day in range(0, 25):
            day_path = mkpath(year_path, "Day {:02d}".format(day + 1))
            if not os.path.isdir(day_path):
                continue

            files = [filename for filename in os.listdir(day_path) if os.path.isfile(mkpath(day_path, filename))]

            if os.path.isfile(mkpath(day_path, "part1.py")):
                solved[year][day][0] = True
            if os.path.isfile(mkpath(day_path, "part2.py")):
                solved[year][day][1] = True

            # Long line warning
            for filename in files:
                if os.path.splitext(filename)[1] == ".py":
                    with open(mkpath(day_path, filename), 'r', encoding="utf-8") as file:
                        for line in file:
                            if len(line.strip()) > 120:
                                print("Warning: long line detected in {}".format(mkpath(day_path, filename)))

            # Handle day README
            if "README.md" not in files:
                continue

            readme_path = mkpath(day_path, "README.md")

            with open(readme_path, 'r', encoding="utf-8") as file:
                readme = file.read()

            # Place non-breaking spaces in markdown `code` tags:
            readme = re.sub(REGEX["markdown_code"], lambda m: m.group(0).replace(" ", " "), readme)

            # readme = readme_exec(readme, path)

            with open(readme_path, 'w', encoding="utf-8") as file:
                file.write(readme)

        # Handle year README
        # TODO

    # Handle global README
    global_readme_table(solved)


if __name__ == "__main__":
    main()
