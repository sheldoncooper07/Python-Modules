import pandas as pd
a=pd.read_excel(r"C:\Users\DIVYA JOSHI\Desktop\weatherreport123.xlsx")
b=a.fillna(0)
print(b)


