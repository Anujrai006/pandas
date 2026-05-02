import pandas as pd
Studnets={
    "Name":["anuj","bibash","chandra","dipak"],
    "Age":[12,13,14,19]
}
df=pd.DataFrame(Studnets,index=['a' ,'b','c','d'])
child=df["Age"]<=14
# print(df[child]["Name"])
# print(df.loc[df["Age"]<=14,"Name"])
# querry=df.query("Age < 14")
# print(querry)
(df.loc["a","Age"])+=3
df.loc[df["Age"]< 15,"result"]="fail"
print(df)