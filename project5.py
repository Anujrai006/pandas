import pandas as pd
num=int(input("Enter the number of students:"))
Students=[]
students={}
for i in range(num):
    name=input("Enter the name:")
    physics=str(input("Enter marks  for physics"))
    chemistry=str(input("Enter marks for chemistry"))
    maths=str(input("Enter marks for maths"))
    total=int(physics)+int(chemistry)+int(maths)
    total=str(total)
    
    # students={
    #     "name":name,
    #     "physics":physics,
    #     "chemistry":chemistry,
    #     "maths":maths,
    #     "total":total
    # }
    with open("data5.csv" ,"a") as f:
        f.write(f"{name},")
        f.write(f"{physics},")
        f.write(f"{chemistry},")
        f.write(f"{maths},")
        f.write(f"{total}, \n")
model=["Name","Physics","Chemistry","Maths","Total"]
df=pd.read_csv("data5.csv",names=model)
print(df)


