from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import csscompressor
import re


WIDTH = 502.4

MARGIN = 16  # = 1em
LINE_HEIGHT = 20  # For font-size = 16px


def get_canvas() -> str:
    with open('page.html', 'r', encoding='utf-8') as file:
        page = file.read()

    main = BeautifulSoup(page, 'lxml').find('main')
    table_styles_tag = main.findChildren('style')
    if table_styles_tag:
        table_styles = table_styles_tag[0].text
        table_styles_tag[0].decompose()
    else:
        table_styles = ''

    for script in main.find_all('script'):
        script.decompose()

    for tag in main.select(', '.join((
        'span.calendar-day',
        'span.calendar-mark-complete',
        'span.calendar-mark-verycomplete',
        'span#calendar-countdown',
    ))):
        tag.decompose()

    for tag in main.select('pre a, pre span'):
        # tag.name = 'span'
        del tag['aria-label']
        del tag['href']

    for string in main.find('pre').find_all(string=True, recursive=False):
        string.replace_with('\n')

    # Warning! Veru hacky solution, but I can not do otherwise
    for tag in main.select('pre > a, pre > span'):
        # lines = ''.join(map(str, tag.contents)).splitlines()

        # last_line_size = len(lines[-1]) - (3 if lines[-1].endswith(' ' * 3) else 0)
        # for i, line in enumerate(lines):
        #     # assert line.endswith(' ' * 3)
        #     lines[i] = line[:last_line_size]

        # tag.clear()

        # tag.append(BeautifulSoup('\n'.join(lines), 'lxml'))

        # last_text = tag.find_all(text=True)[-1]

        # Remove 3 spaces from the end of span
        for _ in range(3):
            string = str(tag.find_all(string=True)[-1])
            if string.endswith(' '):
                string = string[:-1]
                if string:
                    tag.find_all(string=True)[-1].replace_with(string)
                else:
                    tag.find_all(string=True)[-1].extract()

        # Remove 7 spaces before every \n in span
        for _ in range(7):
            for string in tag.find_all(string=re.compile(r'\n')):
                parts = string.split('\n')
                for i in range(len(parts) - 1):
                    if parts[i].endswith(' '):
                        parts[i] = parts[i][:-1]

                string.replace_with('\n'.join(parts))

    for tag in main.descendants:
        if isinstance(tag, Tag):
            if 'aria-hidden' in tag.attrs:
                del tag['aria-hidden']

            tag.attrs = {
                attr: value
                for attr, value in tag.attrs.items()
                if (isinstance(value, str) and value.strip) or value
            }

    main['xmlns'] = 'http://www.w3.org/1999/xhtml'

    # ----------------------------------------------------- STYLES -----------------------------------------------------

    styles = requests.get('https://adventofcode.com/static/style.css').text
    with open('Source Code Pro.css') as file:
        styles = styles.replace(
            "@import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@300');",
            file.read()
        )
    styles += table_styles

    with open('additional_styles.css') as file:
        styles += file.read()

    style_tag = Tag(name='style')
    main.append(style_tag)
    style_tag.string = csscompressor.compress(styles)
    # style_tag.string = styles  # For debugging

    with open('canvas.html', 'w', encoding='utf-8') as file:
        print(str(main), file=file)

    # HACK: Styles for `body` -> styles for `main`
    style_tag.string = style_tag.string.replace('body{', 'main{')

    # ------------------------------------------------------ SVG -------------------------------------------------------

    # Calculate SVG height based on the amount of rows in calendar
    # row_count = len(main.select('pre > a, pre > span'))
    row_count = sum(
        1 + len(tag.find_all(string=re.compile(r'\n')))
        for tag in main.select('pre > a, pre > span')
    )
    height = LINE_HEIGHT * row_count + 2 * MARGIN
    print(f'Rows: {row_count} => Height: {height}')

    foreign_object = Tag(name='foreignObject', attrs={'x': '0', 'y': '0', 'width': '100%', 'height': '100%'})
    foreign_object.append(main)

    svg = Tag(name='svg', attrs={
        'xmlns': 'http://www.w3.org/2000/svg',
        'width': WIDTH,
        'height': height,
        'viewBox': f'0 0 {WIDTH} {height}',
    })
    svg.append(foreign_object)

    canvas = str(svg)
    # canvas = htmlmin.minify(
    #     canvas,
    #     remove_all_empty_space=True,
    #     reduce_boolean_attributes=True,
    #     remove_optional_attribute_quotes=False
    # )
    with open('canvas.svg', 'w', encoding='utf-8') as file:
        print(canvas, file=file)


if __name__ == '__main__':
    get_canvas()
