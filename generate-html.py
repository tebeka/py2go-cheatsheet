#!/usr/bin/env python

from subprocess import check_output
import html
import re
import yaml

find_code = re.compile('code: (\w+)').search

table_html = '''
<table class="code table table-sm">
  <tbody>
  <tr>
    <td class="left">{py}</td>
    <td>{go}</td>
  </tr>
  </tbody>
</table>
'''


module_html = '''
<tr>
  <td>{task}</td>
  <td><a href="https://docs.python.org/3/library/{python}.html">
    {python}</a>
  </td>
  <td><a href="https://golang.org/pkg/{go}/">{go}</a></td>
</tr>
'''

is_start = re.compile(r'(//|#) START').search
is_end = re.compile(r'(//|#) END').search
find_spaces = re.compile('^[ \t]+').match


def indent_size(line):
    match = find_spaces(line)
    return len(match.group()) if match else 0


def get_code(fname, sep):
    blocks = []
    block = []
    in_block = False
    with open(fname) as fp:
        for line in fp:
            if is_start(line):
                assert not in_block, 'start inside block'
                in_block = True
                continue
            elif is_end(line):
                assert in_block, 'end without block'
                blocks.append(block)
                block = []
                in_block = False
            elif in_block:
                block.append(line.replace('\t', '    '))

    for block in blocks:
        indent = min(indent_size(line) for line in block if line.strip())
        for i, line in enumerate(block):
            block[i] = line[indent:]

    codes = [''.join(block).strip() for block in blocks]
    return sep.join(codes)


def code_for(name, typ):
    ext = typ[:2]
    comment = '#' if typ == 'python' else '//'
    sep = '\n\n{} ...\n\n'.format(comment)
    return get_code(f'{name}.{ext}', sep)


def htmlize(code, typ):
    cmd = ['pygmentize', '-l', typ, '-f', 'html']
    return check_output(cmd, input=code.encode()).decode()


def modules():
    with open('modules.yaml') as fp:
        modules = yaml.load(fp)
    for module in modules:
        module['task'] = html.escape(module['task'])
        print(module_html.format(**module))


if __name__ == '__main__':
    from argparse import ArgumentParser, FileType
    from sys import stdin

    parser = ArgumentParser()
    parser.add_argument('--file', type=FileType(), default=stdin)
    args = parser.parse_args()

    for line in args.file:
        line = line[:-1]  # trim newline
        match = find_code(line)
        if match:
            name = match.group(1)
            py = htmlize(code_for(name, 'python'), 'python')
            go = htmlize(code_for(name, 'go'), 'go')
            print(table_html.format(py=py, go=go))
        elif line.strip() == ':modules:':
            modules()
        else:
            print(line)
            continue
