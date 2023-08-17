# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:30:32 2023

@author: erenz
"""

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print(fib(4))