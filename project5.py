
import pandas as pd
num=int(input("Enter the number of students:"))
Students=[]
stored_names=[]
for i in range(num):
    name=input("Enter the name:")
    if name in stored_names:
        print(f"{name} already exists")
        continue
    physics=int(input("Enter marks  for physics"))
    chemistry=int(input("Enter marks for chemistry"))
    maths=int(input("Enter marks for maths"))
    total=physics+chemistry+maths
    # total=str(total)
    
  
    Students.append({
        "name":name,
        "physics":physics,
        "chemistry":chemistry,
        "maths":maths,
        "total":total
    })
    print(f"{name} Saved succesfully 🎉")
    stored_names.append(name)
    # with open("data5.csv" ,"a") as f: code for permanent 
    #     f.write(f"{name},")
    #     f.write(f"{physics},")
    #     f.write(f"{chemistry},")
    #     f.write(f"{maths},")
    #     f.write(f"{total},\n")
# model=["Name","Physics","Chemistry","Maths","Total"]
df=pd.DataFrame(Students)
df.to_csv("data5.csv",index=False)
print(df)


