# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:20:51 2023

@author: erenz
"""

word = input()
vowels = ["a","e","i","o","u"]
a = [i for i in word if i not in vowels]
print(a)

#multiples of 3

b = [i for i in range(20) if i%3==0]

