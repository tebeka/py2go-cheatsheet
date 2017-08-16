from generate import find_code

import pytest

from os import path
from subprocess import check_output
from sys import executable
import re

in_file = None

with open('Makefile') as fp:
    for line in fp:
        match = re.search('html\s*=\s*(.*\.html)', line)
        if match:
            in_file = '{}.in'.format(match.group(1))
            if not path.isfile(in_file):
                raise SystemExit('error: cannot find {}'.format(in_file))
            break
    else:
        raise SystemExit('error: cannot find html in Makefile')


py_files = []
go_files = []
for line in open('cheatsheet.html.in'):
    match = find_code(line)
    if not match:
        continue
    name = match.group(1)
    if name == 'httpd':
        continue  # Runs a server
    py_files.append(f'{name}.py')
    go_files.append(f'{name}.go')


@pytest.mark.parametrize('fname', py_files)
def test_py(fname):
    check_output([executable, fname])


@pytest.mark.parametrize('fname', go_files)
def test_go(fname):
    check_output(['go', 'run', fname])
