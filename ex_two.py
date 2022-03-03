#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:39:22 2022

@author: joseortega
"""

def ex_two(inv_one, inv_two, inv_three):
    total = inv_one + inv_two + inv_three

    p_one = inv_one/total * 100
    p_two = inv_two / total * 100
    p_three = inv_three / total * 100

    return p_one, p_two, p_three


p_one, p_two, p_three = ex_three(2000, 2000, 2000)
print(f'Porcentaje 1: {p_one}')
print(f'Porcentaje 2: {p_two}')
print(f'Porcentaje 3: {p_three}')