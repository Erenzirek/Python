# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 17:20:20 2023

@author: erenz
"""
"""
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()
"""
#This pattern can be used at any time, to wrap any function.
#Python provides support to wrap a function in a decorator 
#by pre-pending the function definition with a decorator
# name and the @ symbol.
#If we are defining a function we can "decorate" it with the
# @ symbol like:
"""    
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text();
"""

def decor(func):
    def f1(*args, **kwargs):
        print("***")
        func(*args, **kwargs)
        print("***")
    return f1

@decor
def invoice(num):
    print("INVOICE #" + num)

invoice(input("Enter invoice number: "))