#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    stroka = (input("Введите строку: ")).lower()
    if len(stroka) == 0:
        print("Введена пустая строка!")
        exit(1)
    vowels = {'а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы'}
    expt = {'.', ' ', '!', '?', ','}
    only_vowels = (set(list(stroka))).difference(expt)
    only_vowels = only_vowels.intersection(vowels)
    if len(only_vowels) == 0:
        print("В строке нет гласных букв!")
    else:
        print(','.join(only_vowels))
        print("Количество гласных в строке: ", len(only_vowels))
