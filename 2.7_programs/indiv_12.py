#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Универсальное множество
    univ = set("abcdef")
    A = {'b', 'k', 'n', 'o', 'q'}
    B = {'a', 'b', 'k', 'u'}
    C = {'o', 'p'}
    D = {'a', 'm', 'n', 'y', 'z'}

    X = (A.union(B)).intersection(D)
    # Взяли дополнение для множества A
    an = univ.difference(A)
    an_int_D = an.difference(D)
    c_diff_b = C.difference(B)

    Y = an_int_D.union(c_diff_b)
    print("A", A, "B", B, "C", C, "D", D)
    print("X = (A ∪ B) ∩ D => ", X)
    print("Y = (¬A ∩ D) ∪ (C / B) =>", Y)
