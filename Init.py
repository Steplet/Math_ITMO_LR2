import Tangent_file as te
import Chord_file as ch
import Newtons_file as new

def init_methods():
    file_equ = open("Equations", "r")
    equation = file_equ.readline()

    a, b = 1, 4

    res_chord, counter_chord = ch.chord_method(equation, a, b)
    res_tan, counter_tan = te.tangent_method(equation, b)

    print("Chord method")
    print('Iter', counter_chord)
    print('Root', res_chord)

    print("Tangent method")
    print('Iter', counter_tan)
    print('Root', res_tan, '\n')

    print('Difference of roots', abs(res_chord - res_tan), '\n')

    lines = new.get_lines()

    x_0 = [0.5, 0.5, 0.5]

    res_new, counter_newton = new.newtons_method(lines, x_0)
    print("Newtons method")
    print("Iter", counter_newton)
    for i in range(len(res_new)):

        print('x_' + str(i) + ' =', res_new[i])
