# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 17:03:11 2023

@author: erenz
"""

def infinite_sevens():
  while True:
    yield 7
        
for i in infinite_sevens():
  print(i)
  
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))