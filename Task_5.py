# С помощью list comprehension

# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

import os
import random

# Старое решение задачи
# def main():
#     os.system('cls')
#     num = int(input('Введите число N: '))
#     for i in range(num):
#         print(random.randint(-100, 100), end=', ')

# Новое решение задачи


def main():
    print(*[random.randint(-100, 100) for _ in range(int(input('Введите число N: ')))])


if __name__ == '__main__':
    main()
