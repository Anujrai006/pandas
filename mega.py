import pandas as pd
df=pd.read_csv("mega.csv")
for x in (["English","Math","Science","Nepali","Computer"]):
 df[x]=df[x].fillna(df[x].mean())
df["Attendance"]=df["Attendance"].fillna(df["Attendance"].median())
df["Total"]=df["English"]+df["Science"]+df["Math"]+df["Nepali"]+df["Computer"]
df["Total"]=df["Total"].astype(int)
df["Percentage"]=(df["Total"]/500)*100 
df["Percentage"]=df["Percentage"].astype(str) + "%"
print(df)