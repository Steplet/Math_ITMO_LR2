import math as m
import copy
import sympy
import re
import numpy as np

import Diff_file
import Parser as p
import Tangent_file


def get_lines():
    file = open("For Newtons", "r")

    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')


    return lines

def diff_newtons(line, arg):
    x = sympy.symbols('x' + str(arg + 1))

    copy_line = copy.deepcopy(line)

    copy_line = copy_line.replace('tg', 'tan')
    copy_line = copy_line.replace('ctg', 'cot')

    res = sympy.diff(copy_line, x)
    res = str(res)
    res = re.sub(r'(?<=\d)\*(?=\w)|(?<=\w)\*(?=\d)|(?<=\w)\*(?=\w)|(?<=\d)\*(?=\d)', ' * ', res)
    # res = re.sub(r'-', ' - ')

    return res

def calc_newtons(line, args, len_x_args):
    x = args
    temp = copy.deepcopy(line)

    for i in range(len_x_args):

        temp = re.sub('x'+str(i+1), str(args[i % len_x_args]), temp)

    temp = p.pars(temp)
    res = eval(temp)
    return res




def newtons_method(lines, x_args, e=0.00001):
    x_0 = []
    l = len(lines)
    for i in range(len(x_args)):
        x_0.append(x_args[i])

    x_0 = np.array(x_0)
    W = []

    t = 0

    for i in range(len(lines) * len(lines)):
        if i % l == 0 and i != 0:
            t += 1
        W.append(lines[t])


    t = 0

    for i in range(len(lines) * len(lines)):
        if i % l == 0 and i != 0:
            t += 1
        W[i] = diff_newtons(lines[t], i % l)
    # print('W', W)

    local_e = 1
    counter = 0

    while local_e > e and counter < 20:
        counter += 1

        W_i = []

        for i in range(len(lines) * len(lines)):
            W_i.append(calc_newtons(W[i], x_0, l))



        F = []

        for i in range(l):
            F.append(calc_newtons(lines[i], x_0, l))

        W_i_np = np.array_split(W_i, l)
        W_i_np = np.array(W_i_np)

        F_np = np.array(F)
        F_np = F_np * -1

        delta_x = np.linalg.solve(W_i_np, F_np)

        x_0 = x_0 + delta_x

        for i in range(len(delta_x)):
            if abs(delta_x[i]) > local_e:
                local_e = abs(delta_x[i])


    return x_0, counter


