# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:39:08 2023

@author: erenz
"""

numbers = (1,2,3)
a,b,c = numbers
print(a)
print(b)
print(c)

x,y = [1,2]
x,y = y,x
print(y)

a, b, c, d, *e, f, g = range(20)
print(len(e))

#Sets cannot contain duplicate elements.
num_set = {1, 2, 3, 4, 5}
print(3 in num_set)

letters = {"a", "b", "c", "d"}
if "e" not in letters:
  print(1)
else: 
  print(2)
