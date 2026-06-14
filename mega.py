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
fail_atd=(df["Attendance"]<75).value_counts()
print(f" no of students who failed due to attendance are {fail_atd[True]}")
# min_avg_marks="Computer"
x = ["Computer","English","Nepali","Science","Math"]
average_marks=df[x].mean()
average_min=average_marks.idxmin()
print(f"Lowest scoring sub: {average_min}")
failed=df[df["Grade"]=="Fail"]
print(f" failes students :{failed["Name"]}")
s=df[df["Attendance"]==100]
print(f"100% attensance {s["Name"]}")
sorted_per=df.sort_values(by="Percentage",ascending=False)
print(sorted_per[["Name","Percentage"]])
d=df.groupby(("Gender"))
print(d["Name"])
female=df.groupby("Gender").get_group("Female")
result_female=female[female["Grade"].isin(["A",'A+'])]
print(result_female["Name"])
# print(df)
def new_func(df):
    passed=df[df["Status"]=="Pass"]
    print(passed)
    ktm=passed[passed["City"]=="Kathmandu"]
    print(ktm[["Name","Grade"]])
def avg_per_city(x):
   gend_by_std=x.groupby("City")["Percentage"].mean()
   print(gend_by_std)
avg_per_city(df)
def gender_by_grade(x):
   student=x.groupby("Gender")
   print(student["Grade"].value_counts())
gender_by_grade(df)
def top(x):
   sorted=x.sort_values(by='Percentage',ascending=False)
   sorted.head(3).to_csv("Toppers.csv",index=False)
   students=sorted.groupby("City")
   
   print(students[["Name","Percentage"]].head(2))
top(df)
df.to_csv("Clean_data.csv",index=False)
failed.to_csv("failed_stds.csv",index=False)

