import pandas as pd
df=pd.read_csv("data.csv",index_col="Name")
# lst=["Name","Height","Weight"]
# print(df.loc[1])
print(df.loc["Charizard":"Blastoise",["Weight","Height"]])
print(df.iloc[0:4,0:2])