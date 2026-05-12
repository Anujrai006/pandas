import pandas as pd
df=pd.read_csv("project.csv")
# # print(df.head())

df["Math"]=df["Math"].fillna(df["Math"].mean())
print(df)
print(df.columns)