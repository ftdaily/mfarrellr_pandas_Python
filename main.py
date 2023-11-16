# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:12:48 2023

@author: flummox
"""

import pandas as pd

data = pd.read_excel("nilai.xlsx")

a = input("Sheet a atau b: ")

if a == "a":
    pd.set_option('display.max_rows', None)
    print(pd.read_excel("nilai.xlsx", sheet_name="Sheet1"))
else:
    pd.set_option('display.max_rows', None)
    print(pd.read_excel("nilai.xlsx", sheet_name="Sheet2"))



