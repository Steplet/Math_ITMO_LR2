import copy
import math as m
import Diff_file as d
import Parser as p

def tan_calc(line, arg):
    x_0 = arg
    temp = line.replace('x', 'x_0')
    res = eval(temp)
    return res


def tangent_method(line, arg_x, e=0.001):
    fun_0 = copy.deepcopy(line)
    fun_0 = p.pars(fun_0)
    fun_1 = d.simple_diff(line)
    fun_1 = p.pars(fun_1)

    x = copy.deepcopy(arg_x)
    x_0 = 0
    locale_e = 1
    counter = 0

    while locale_e > e:
        counter += 1

        x_0 = x

        x = x_0 - (tan_calc(fun_0, x_0) / tan_calc(fun_1, x_0))

        locale_e = abs(x_0 - x)

    return x, counter






