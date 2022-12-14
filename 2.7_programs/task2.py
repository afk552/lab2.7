#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    strr1 = input("Введите первую строку: ").lower()
    strr2 = input("Введите вторую строку: ").lower()
    set_inter = set(strr1).intersection(set(strr2))
    expt = {'.', ' ', '!', '?', ','}
    set_inter = set_inter.difference(expt)
    if len(set_inter) > 0:
        print("Общие символы в двух строках: ", ' '.join(set_inter))
    else:
        print("В строках нет общих символов!")
