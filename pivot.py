import pandas as pd
a=pd.read_csv(r"C:\Users\DIVYA JOSHI\Desktop\weatherreport123.csv")
df=pd.DataFrame(a)
b=df.pivot(index="date",columns="city")
print(b)