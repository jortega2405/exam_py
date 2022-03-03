#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:31:05 2022

@author: joseortega
"""

def ex_five(redes, cont, dis):
    total = redes+cont+dis
    per_redes= (redes/total)*100
    per_cont= (cont/total)*100
    per_dis= (dis/total)*100
    
    print('el porcentaje para redes es: ', per_redes)
    print('el porcentaje para redes es: ', per_cont)
    print('el porcentaje para redes es: ', per_dis)
    
ex_five(20, 50, 20)