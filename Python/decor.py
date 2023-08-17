# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 17:42:20 2023

@author: erenz
"""

def decor(func):
    def wrap(num):
        print("***")
        func(num)
        print("***")
        print("END OF PAGE")
    return wrap

@decor
def invoice(num):
    print("INVOICE#"+num)
    
invoice(input())