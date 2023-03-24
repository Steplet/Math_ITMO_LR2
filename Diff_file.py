import copy
import re

from sympy import cos, sin, tan, ln, cot, log, Symbol
import sympy


def simple_diff(line):
    x = Symbol('x')
    copy_line = copy.deepcopy(line)

    copy_line = copy_line.replace('tg', 'tan')
    copy_line = copy_line.replace('ctg', 'cot')
    # copy_line = copy_line.replace('*', ' * ')

    res = sympy.diff(copy_line)
    res = str(res)
    res = re.sub(r'(?<=\d)\*(?=\w)|(?<=\w)\*(?=\d)|(?<=\w)\*(?=\w)|(?<=\d)\*(?=\d)', ' * ', res)

    return res
