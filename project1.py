#series from dictionary which temp store data of students and list out in table of 1-d
import pandas as pd
students_info={"Name:":"Marks:"}
n=int(input("Enter the  no of stds:"))
for i in range(n):
    name=input("enter the name:")
    marks=int(input("enter the marks:"))
    students_info[name]=marks
# print(students_info)
students_data=pd.Series(students_info)
print(students_data)