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
df.loc[df["Attendance"]>=75,"Status"]="Pass"
df.loc[df["Attendance"]<75,"Status"]="Fail"
top_idx=df["Percentage"].idxmax()
print("Result of class 11:")
print(f"Topper is : {df.loc[top_idx,"Name"]} with {df.loc[top_idx,"Percentage"]}%")
low_idx=df["Percentage"].idxmin()
print(f"lopper is : {df.loc[low_idx,"Name"]} with {df.loc[low_idx,"Percentage"]}%")
print(df["Grade"].value_counts())
print("average percentage by gender:")
print(df.groupby("Gender")["Percentage"].mean())
avg_city=df.groupby("City")["Percentage"].mean()
# city_max=df[avg_city,"Percentage"].idxmax()
city_max=avg_city.idxmax()
print(f"Highest scoring city is {city_max}")