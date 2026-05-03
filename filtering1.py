import pandas as pd
Studnets={
    "Name":["anuj","bibash","chandra","dipak"],
    "Age":[12,13,14,19],
    "Physics":[10,11,23,22],
    "Chemistry":[21,22,12,29]

}
df=pd.DataFrame(Studnets,index=['a' ,'b','c','d'])
child=df["Age"]<=14
# print(df[child]["Name"])
# print(df.loc[df["Age"]<=14,"Name"])
# querry=df.query("Age < 14")
# print(querry)
(df.loc["a","Age"])+=3
df["Percentage"]=((df["Physics"]+df["Chemistry"])/60)*100
df.loc[df["Percentage"]< 60,"result"]="fail"
df.rename(columns={"result":"results"},inplace=True)
# df.drop("Age",axis=1,inplace=True)
df["Age"].replace(15,13,inplace=True)
print(df)
