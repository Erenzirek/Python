# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:31:24 2023

@author: erenz
"""

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))


"""
price = int(input())
perc = int(input())
res = (lambda x,y:x*y/100)(price, perc)
print(res)
"""
a = (lambda x: x*x)(8)
print(a)