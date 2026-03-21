#creating the data frame of students name and class . (list to updating into DF)
import pandas  as pd
import numpy as np
students=[]  
n=int(input("Enter the no of stds:"))
for i in range(n+1):
    name=input("Enter the name:")
    Class=int(input("enter the class"))
    # students["name"]=name
    # students["class"]=Class
    data={"name":name,"class":Class}
    students.append(data)
print(students)
df=pd.DataFrame(students,index=[f"student{i}:" for i in range(n+1)])
print(df)

    # students.update(dict2)

    
    



