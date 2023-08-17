# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:16:32 2023

@author: erenz
"""
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))