import pandas as pd
df=pd.read_csv("data8.csv")
df["Total"]=df["Math"]+df["Science"]+df["English"]
df["Average"]=df["Total"]/3
df["Results"]=df.apply(lambda x:"pass" if(x["Math"]>=60 and x["Science"] >=60 and x["English"] >=60) else "Fail",axis=1)
top_students=df[df["Average"]>=80]
print(f"Toppers :\n {top_students["Name"]}")
print(f"Students :\n {df}")