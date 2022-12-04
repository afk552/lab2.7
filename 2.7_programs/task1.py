#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    stroka = (str(input("Введите строку: "))).lower()
    vowels = {'а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы'}
    expt = {'.', ' ', '!', '?', ','}

    only_vowels = (set(list(stroka))).difference(expt)
    only_vowels = only_vowels.intersection(vowels)
    print(only_vowels)
    print("Количество гласных в строке: ", len(only_vowels))
