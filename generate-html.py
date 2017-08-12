#!/usr/bin/env python

from sys import stdin
import re
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


def get_code(fname, sep):
    lines = []
    in_block = False
    nblocks = 0
    lnum = 0
    with open(fname) as fp:
        for line in fp:
            if is_start(line):
                assert not in_block, 'start inside block'
                nblocks += 1
                in_block = True
                continue
            elif is_end(line):
                assert in_block, 'end without block'
                lnum = 0
                in_block = False
            elif in_block:
                if nblocks > 1 and lnum == 0:
                    lines += sep
                lines.append(line)
                lnum += 1

    # tab -> space
    lines = [line.replace('\t', '    ') for line in lines]

    # Drop indent
    # FIXME: Do it per block
    indent = min(indent_size(line) for line in lines)
    code = ''.join(line[indent:] for line in lines)
    return code.strip()


def code_for(name, typ):
    ext = typ[:2]
    comment = '#' if typ == 'python' else '//'
    sep = ['\n', '{} ...\n'.format(comment), '\n']
    return get_code(f'{name}.{ext}', sep)


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
