#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:49:31 2022

@author: joseortega
"""

def ex_three(base_salary, sales):
    comision = sales * 0.15
    total_payment = base_salary + comision

    return f'El total de venta fue {sales}, con una comision de {comision}, el total a pagar es {total_payment}'


print(ex_three(10000, 10000))