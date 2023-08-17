# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:36:01 2023

@author: erenz
"""

def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)