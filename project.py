import pandas as pd
df=pd.read_csv("project.csv")
# # print(df.head())

df["Math"]=df["Math"].fillna(df["Math"].mean())
df["Science"]=df["Science"].fillna(df["Science"].mean())
df["English"]=df["English"].fillna(df["English"].mean())
df["Total"]=df["Math"]+df["English"]+df["Science"]
df["Average"]=df["Total"]/3
for x in range(len(df)):
 if df.loc[x,"Average"] >=90:
    df.loc[x,"Grade"]="A+"
 elif df.loc[x,"Average"] >=80 and df.loc[x,"Average"]<90:
    df.loc[x,"Grade"]="A"
 else:
    df.loc[x,"Grade"]="fail"
hmax=df["Average"].idxmax()
Math_max=df["Math"].idxmax()
print(df)
print("Overal topper:\b")
print(df.loc[hmax,"Name"])
print("Math Topper:\b")
print(df.loc[Math_max,"Name"])