# С помощью использования map

# 1. Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# Старое решение:

# text = list(map(int, input('Введите числа через пробел: ').split()))
# text.sort()
# print(text[0], text[-1])

# Новое решение (искусственно усложненное :) ):
def main():
    text = input('Введите числа через пробел: ').split()
    for index in range(len(text)):
        text[index] = int(text[index])
    print(min(text), max(text))


if __name__ == '__main__':
    main()