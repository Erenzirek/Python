# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:16:50 2023

@author: erenz
"""
def convert(num): 
 if num==0:
     return 0
 return (num % 2 + 10 * convert(num // 2)) 

a = int(input())
print(convert(a))