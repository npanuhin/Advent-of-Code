def table_to_html(table: list[list], headers_on: bool = False) -> str:
    table_result = []

    for line_num, line in enumerate(table):
        item_tag = 'th' if headers_on and line_num == 0 else 'td'

        line_result = []

        for item in line:
            if isinstance(item, (tuple, list)):
                line_result.append(wrap_tag(item_tag, item[0], tag_args=item[1]))
            else:
                line_result.append(wrap_tag(item_tag, item))

        table_result.append(wrap_tag('tr', '\n'.join(line_result), inline=False))

    return wrap_tag('table', '\n'.join(table_result), inline=False)


def wrap_tag(tag: str, content: str, inline: bool = True, tag_args: dict[str, str] = None) -> str:
    if content is None:
        content = ''

    args = ' '.join(f'{key}="{value}"' for key, value in (tag_args or {}).items())
    if args:
        before = f'<{tag} {args}>'
    else:
        before = f'<{tag}>'
    after = f'</{tag}>'

    if inline:
        return f'{before}{content}{after}'

    content = '\n'.join('\t' + line for line in content.splitlines())
    return f'{before}\n{content}\n{after}'


def html_link(text: str, link: str, tag_args: dict[str, str] = None) -> str:
    if tag_args is None:
        tag_args = {}
    tag_args['href'] = link
    return wrap_tag('a', text, tag_args=tag_args)
    # return f'<a href="{link}">{text}</a>'


if __name__ == '__main__':  # Tests
    table = [
        [
            ['a', {'align': 'center'}],
            'b',
            'c'
        ],
        ['d', 'e', 'f', ('g', {'colspan': -1, 'align': 'left'})],
        [('h', {'colspan': 2}), 'i'],
    ]
    print(table)
    print(table_to_html(table, True))
    assert table_to_html(table, True) == '\n'.join((
        '<table>',
        '\t<tr>',
        '\t\t<th align="center">a</th>',
        '\t\t<th>b</th>',
        '\t\t<th>c</th>',
        '\t</tr>',
        '\t<tr>',
        '\t\t<td>d</td>',
        '\t\t<td>e</td>',
        '\t\t<td>f</td>',
        '\t\t<td colspan="-1" align="left">g</td>',
        '\t</tr>',
        '\t<tr>',
        '\t\t<td colspan="2">h</td>',
        '\t\t<td>i</td>',
        '\t</tr>',
        '</table>'
    ))
