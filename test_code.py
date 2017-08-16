from generate import find_code

import pytest

from subprocess import check_output
from sys import executable

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
