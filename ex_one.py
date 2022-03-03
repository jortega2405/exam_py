#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:15:12 2022

@author: joseortega
"""


def ex_one(donation):
    tel= donation * 0.1
    sis= donation * 0.25
    admin = donation * 0.35
    cont = donation - (tel + sis + admin)
    
    print('El porcentaje que le toca a telco es:', tel)
    print('El porcentaje que le toca a sistemas es:', sis)
    print('El porcentaje que le toca a administracion es:', admin)
    print('El porcentaje que le toca a contabilidad es:', cont)
    
ex_one(1000)
   
