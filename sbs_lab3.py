#!/usr/bin/env python3
# coding=utf-8

# Имеется двумерный массив 4x5. Реализовать возможность заполнения его
# случайными числами. Реализовать команду выполнить задание, которая выполняет:
# Если во втором столбце стоят две единицы, то уменьшить макс. элемент первой
# строки в два раза, а все единицы в таблице заменить нулями.

import random  # импортируем модуль random для генерации случайных чисел


# Функция генерирует nxm массив случайных чисел до max_value, у которого
# стандартное значение 20
def random_array(n, m, max_value=20):
    array = []  # инициализируем массив
    # Цикл for. Оператор range выдает диапазон чисел, в данном случае
    # от 0 до n-1
    for i in range(0, n):
        sub_array = []  # инициализируем подмассив
        # Если передать range один аргумент, то нижняя граница 0, в данном
        # случае диапазон чисел будет от 0 до m-1
        for j in range(m):
            # Генерируем слуйчаное число от 0 до 19 и добавляем его в подмассив
            number = random.randint(0, max_value)
            sub_array.append(number)
        # Добавляем полученный подмассив в основной массив
        array.append(sub_array)
    return array  # возвращаем массив из случайных чисел


def print_array(array):  # функция выводит массив в удобочитаемой форме
    print()  # переход на новую строку
    # Циклу for также можно давать массивы, тогда перебирается каждый элемент
    for i in array:
        # Так как массив состоит из подмассивов, тогда каждый элемент тоже
        # можно перебрать используя цикл for
        for j in i:
            print("%d\t" % j, end='')  # выводим каждое значение и табуляцию
        print()  # переход на новую строку


def main():
    array = random_array(4, 5)  # заполняем массив случайными числами
    print_array(array)  # выводим массив на экран
    # Бесконечный цикл while, который закончится только при помощи break
    while True:
        print  # переход на новую строку
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        # Получаем ввод команды от пользователя
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # если команда 1, то заполняем массив заново
            array = random_array(4, 5)
            print_array(array)
            # После этого условия цикл начнется с начала
        elif key == '2':  # если команда 2, то проверяем условие
            print()  # переход на новую строку

            #Ищу В какой строке находится максимальный элемент
            max_1str = -1
            max_2str = -1
            max_3str = -1
            max_4str = -1

            for i in array[0]:
                if i > max_1str:
                    max_1str = i

            for i in array[1]:
                if i > max_2str:
                    max_2str = i

            for i in array[2]:
                if i > max_3str:
                    max_3str = i

            for i in array[3]:
                if i > max_4str:
                    max_4str = i
            #Если максимальный элемент находится в последней строке, то
            #увеличить все элементы первого столбца в 2 раза
            if max_4str > max_3str and max_4str > max_2str and max_4str > max_1str:
                array[0][0] = array[0][0]*2
                array[1][0] = array[1][0] * 2
                array[2][0] = array[2][0] * 2
                array[3][0] = array[3][0] * 2

                print("00000 максимальный элемент в последней строке")
            else:
                print("Максимальный элемент не находится в последней строке")

                print()

                # Выводим на экран результаты

            print_array(array)

        elif key == '3':
            exit(0)  # выходим из программы


if __name__ == '__main__':
    main()
