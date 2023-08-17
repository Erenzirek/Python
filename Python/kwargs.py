# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:39:18 2023

@author: erenz
"""

def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

def example_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

example_function(name="Alice", age=30, city="New York")