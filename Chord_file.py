import copy
import math as m
import Parser as p

def calc(line, arg):

    a = arg
    temp = line.replace('x', 'a')
    res = eval(temp)
    return res


def chord_method(line, arg_a, arg_b, e=0.001):
    line = p.pars(line)

    a = copy.deepcopy(arg_a)
    b = copy.deepcopy(arg_b)

    local_e = 1
    counter = 0
    x_prev = 0
    x = 0

    while local_e > e:
        counter += 1
        x_prev = x

        x = a - ((calc(line, a)) / (calc(line, b) - calc(line, a))) * (b - a)

        if calc(line, x) * calc(line, b) < 0:
            a = x

        if calc(line, a) * calc(line, x) < 0:
            b = x

        local_e = abs(x - x_prev)

    return x, counter
