from learning import working_with_neurons, learning1, print_num, recovering
import os
from os.path import isfile

example_for_learning = "example_for_learning"
incorrect_variant = "incorrect_variant.txt"

max_side = 512
side_of_num = 8
symbols_for_coding = {'.': -1, '#': 1}


# перевод картинки в массив из 1 и -1
def loading(dir):
    file_with_numbers = []
    for filename in os.listdir(dir):
        path = os.path.join(dir, filename)
        if isfile(path):
            file_with_numbers.append(path)

    numbers = []
    for path in file_with_numbers:
        with open(path) as f:
            contents = f.read(max_side)
            contents = str.replace(contents, "\n", "")
            contents = str.replace(contents, "\r", "")
            numbers.append([symbols_for_coding[c] for c in contents])
    return numbers


def main():
    numbers = loading(example_for_learning)
    with open(incorrect_variant) as f:
        contents = f.read(max_side)
        contents = str.replace(contents, "\n", "")
        contents = str.replace(contents, "\r", "")
        numb = [symbols_for_coding[sign] for sign in contents]

    print("Картинки для обучения:")
    for i in numbers:
        print_num(i, side_of_num)
        print()

    print("Процесс обучения")
    working_with_neurons(side_of_num)
    for each_list in numbers:
        learning1(each_list)
    print()

    print("Поломанная картинка")
    print_num(numb, side_of_num)
    print()

    print("Процесс восстановления")
    (recognize, wrong_num, iters) = recovering(numb, side_of_num)
    print()

    print(f"Цифра была восстановлена за {iters} итераций:") if recognize else print(f"Ошибка! Номер проблемной итерации: {iters} ")
    print_num(wrong_num, side_of_num)


if __name__ == '__main__':
    main()