# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:27:19 2018

@author: DIVYA JOSHI
"""

import pandas as pd
a=pd.read_csv(r"C:\Users\DIVYA JOSHI\Desktop\username.csv",header=1,names=["Name","Fathername","mothername"])
c=a.set_index("Fathername")
print(c)
a=pd.read_excel(r"C:\Users\DIVYA JOSHI\Desktop\weatherreport12.xlsx",na_values={"temp":"normal","wind speed":"NAN"})
print(a)
a.to_excel(r"C:\Users\DIVYA JOSHI\Desktop\weatherreport123.xlsx")