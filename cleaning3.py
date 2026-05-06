import pandas as pd
df=pd.read_csv("data.csv")
df.dropna(axis=0,inplace=True)
df.fillna({"Weight":49},inplace=True)
# print(df["Name"].to_string())

# print(df.to_string())