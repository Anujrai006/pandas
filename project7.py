import pandas as pd
# storing data of students using data frames and csv file in pandas/python
df=pd.read_csv("data_7.csv")
# print(df)
Total=df[["Phy","Chem","Math"]].sum(axis=1)
# print(Total)
df["Total"]=Total
print(df)
Class=df.groupby("Class")
top_inx=Class["Total"].idxmax()
print(df.iloc[top_inx])