import random
import math


next_steps = False
W = []  # матрица весов
Y = []
numbers = []
max_iters = 300
current = 0
using_neurons = 0


def char_for(x):
    symbols_for_decoding = {-1: '.', 1: '#'}
    return symbols_for_decoding[x]


def print_num(image, size):
    i = 0
    for symb in image:
        print(f"{char_for(symb)}", end='')
        i += 1
        if i % size == 0:
            print('\n')
    # print('\n')


def working_with_neurons(side):
    global using_neurons, W
    using_neurons = int(math.pow(side, 2))
    for i in range(0, using_neurons):
        W.append([0 for _ in range(0, using_neurons)])


def learning1(number):
    global using_neurons, W, numbers
    numbers.append(number)
    X = number
    for i in range(0, using_neurons):
        for j in range(0, using_neurons):
            if i == j:
                W[i][j] = 0
            else:
                W[i][j] += X[i] * X[j]


def recovering(number, side):
    global Y, max_iters
    Y = number
    iter = 0
    print('Процесс восстановления по нейронам: ')
    while numbers.count(Y) == 0:
        steps_of_recovering(side)
        iter += 1
        if current >= max_iters:
            print(current)
            return False, Y, iter
    return True, Y, iter


def steps_of_recovering(side):
    global current, Y, using_neurons, next_steps
    sign = lambda x: -1 if x < 0 else 1  # задаем функцию активаци
    diapason = random.randrange(0, using_neurons, 1)
    net = 0
    for i in range(0, using_neurons):
        net += Y[i] * W[i][diapason]
    if sign(net) != Y[diapason]:
        print(f'Нейрон {diapason}: с {Y[diapason]}  на  {sign(net)}')
        Y[diapason] = sign(net)
        if next_steps:
            print_num(Y, side)
        current = 0
    else:
        current += 1
