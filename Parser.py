import math as m
import copy
import re


def pars(fun):
    temp = copy.deepcopy(fun)

    temp = temp.replace('^', '**')
    if re.search(r'(?<=\D)e|(?<=\b)e', fun):
        temp = re.sub(r'(?<=\D)e|(?<=\b)e', 'm.e', temp)
    # temp = temp.replace('e', 'm.e')

    if re.search(r'ln|lg|log\(.*?\)', fun):
        list_res = re.findall(r'[^m.-]?lg\(.*?\)|[^m.-]?ln\(.*?\)|[^m.-]?log\(.*?\)', temp)

        list_res_modified = copy.deepcopy(list_res)
        for i in range(len(list_res)):
            split_char = list(list_res[i])
            if split_char[0] == ' ':
                list_res[i] = re.sub(" ", '', list_res[i], count=1)
            list_res_modified[i] = list_res[i]

            list_res_modified[i] = list_res_modified[i].replace('(', '\\(')
            list_res_modified[i] = list_res_modified[i].replace(')', '\\)')
            list_res_modified[i] = list_res_modified[i].replace('+', '\\+')
            list_res_modified[i] = list_res_modified[i].replace('-', '\\-')
            list_res_modified[i] = list_res_modified[i].replace('*', '\\*')

        while len(list_res) != 0:
            x_left_arg = re.sub(r'ln\(|lg\(|log\(', '', list_res[0])
            x_arg = re.sub(r'\)', '', x_left_arg)
            if re.search(r'ln', list_res[0]):
                l = ', m.e)'
            elif re.search(r'lg', list_res[0]):
                l = ', 10)'
            else:
                left = re.sub(r'.*, ', '', list_res[0])
                l = ')'

            temp = re.sub(list_res_modified[0], 'm.log(' + x_arg + l, temp)

            list_res.pop(0)
            list_res_modified.pop(0)

    if re.search(r'(cos|tg|ctg|sin)\(.*?\)', fun):

        list_res = re.findall(r'[^m.]?cos\(.*?\)|[^m.]?tg\(.*?\)|[^m.]?ctg\(.*?\)|[^m.]?sin\(.*?\)', temp)

        list_res_modified = copy.deepcopy(list_res)
        for i in range(len(list_res)):
            split_char = list(list_res[i])
            if split_char[0] == ' ':
                list_res[i] = re.sub(" ", '', list_res[i], count=1)
            list_res_modified[i] = list_res[i]

            list_res_modified[i] = list_res_modified[i].replace('(', '\\(')
            list_res_modified[i] = list_res_modified[i].replace(')', '\\)')
            list_res_modified[i] = list_res_modified[i].replace('+', '\\+')
            list_res_modified[i] = list_res_modified[i].replace('-', '\\-')
            list_res_modified[i] = list_res_modified[i].replace('*', '\\*')

        while len(list_res) != 0:

            temp = re.sub(list_res_modified[0], 'm.' + list_res[0], temp)

            list_res.pop(0)
            list_res_modified.pop(0)

    return temp
