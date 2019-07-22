import pandas as pd
a=pd.read_csv(r"C:\Users\DIVYA JOSHI\Desktop\abcdef.csv")
b=pd.crosstab(a.Gender,a.Age)
print(b)