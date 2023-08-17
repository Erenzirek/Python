# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:18:56 2023

@author: erenz
"""

#What does this list comprehension create?

nums = [i*2 for i in range(10)]
print(nums)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)