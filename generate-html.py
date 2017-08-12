#!/usr/bin/env python

from sys import stdin
import re
from itertools import dropwhile, takewhile
from subprocess import check_output

find_code = re.compile('code: (\w+)').search

table = '''
<table class="code">
  <tr>
    <th>Python</th>
    <th>Go</th>
  </tr>
  <tr>
    <td>{py}</td>
    <td>{go}</td>
  </tr>
</table>
'''

is_start = re.compile(r'(//|#) START').search
is_end = re.compile(r'(//|#) END').search
find_spaces = re.compile('^\s+').match


def indent_size(line):
    match = find_spaces(line)
    return len(match.group()) if match else 0


def get_code(fname):
    with open(fname) as fp:
        lines = dropwhile(lambda line: not is_start(line), fp)
        lines = takewhile(lambda line: not is_end(line), lines)
        next(lines)  # Drop START line
        lines = list(lines)

    # tab -> space
    lines = [line.replace('\t', '    ') for line in lines]

    # Drop indent
    indent = min(indent_size(line) for line in lines)
    code = ''.join(line[indent:] for line in lines)
    return code.strip()


def code_for(name, typ):
    ext = typ[:2]
    return get_code(f'{name}.{ext}')


def htmlize(code, typ):
    cmd = ['pygmentize', '-l', typ, '-f', 'html']
    return check_output(cmd, input=code.encode()).decode()


if __name__ == '__main__':
    for line in stdin:
        line = line[:-1]  # trim newline
        match = find_code(line)
        if not match:
            print(line)
            continue
        name = match.group(1)
        py = htmlize(code_for(name, 'python'), 'python')
        go = htmlize(code_for(name, 'go'), 'go')
        print(table.format(py=py, go=go))
