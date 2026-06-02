import pandas as pd
df=pd.read_csv("mega.csv")
for x in (["English","Math","Science","Nepali","Computer"]):
 df[x]=df[x].fillna(df[x].mean())
df["Attendance"]=df["Attendance"].fillna(df["Attendance"].median())
df["Total"]=df["English"]+df["Science"]+df["Math"]+df["Nepali"]+df["Computer"]
df["Total"]=df["Total"].astype(int)
df["Percentage"]=(df["Total"]/500)*100 
# df["Percentage"]=df["Percentage"].astype(str) + "%"
df.loc[(df["Percentage"]>=90) ,"Grade"]="A+"
df.loc[(df["Percentage"]>=80) & (df["Percentage"]<90),"Grade"]="A"
df.loc[(df["Percentage"]>=70) & (df["Percentage"]<80),"Grade"]="B+"
df.loc[(df["Percentage"]>=60) & (df["Percentage"]<70),"Grade"]="B"
df.loc[(df["Percentage"]>=50) & (df["Percentage"]<60),"Grade"]="C+"
df.loc[(df["Percentage"]>=40) & (df["Percentage"]<50),"Grade"]="C"
df.loc[df["Percentage"]<40,"Grade"]="Fail"

print(df)