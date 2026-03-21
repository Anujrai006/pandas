import pandas  as pd
import numpy as np
data=[]
students=[]

        

    
n=int(input("Enter the no of stds:"))
for i in range(2):
    name=input("Enter the name:")
    Class=int(input("enter the class"))
    # students["name"]=name
    # students["class"]=Class
    data={"name":name,"class":Class}
    students.append(data)
print(students)
df=pd.DataFrame(students,index=[for i in range(n),f"students{i}"])
print(df)

    # students.update(dict2)

    
    



