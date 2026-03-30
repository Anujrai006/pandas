import pandas as pd
# storing data of students using data frames and csv file in pandas/python
df=pd.read_csv("data_7.csv")
# print(df)
Total=df[["Phy","Chem","Math"]].sum(axis=1)
# print(Total)
df["Total"]=Total
# print(df)
Class=df.groupby("Class")
top_inx=Class["Total"].idxmax()
print("TOPPERS:")
toppers=(df.iloc[top_inx])
print(toppers)
topper_names=toppers["Name"]
for name in topper_names:
    print(f"Congratulation {name}🎉🎉")

print('FAILED STUDENTS')
failed_students=df[df["Total"]<75]
print(failed_students)
    