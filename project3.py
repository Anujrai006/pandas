import pandas as pd
while True:
 choice=input("Do you wnat to store data again:Yes,No:")
 if "yes" in choice.lower():
    with open("data3.csv","a") as f:
     for i in range(4):
        no=str(i+1)
        name=input("Enter the name:")
        Class=input("Enter the class:")
        roll_no=input("Enter the roll no:")
        f.write(no+"," + name +"," + Class +"," + roll_no+ "\n")
 else:
   break
df=pd.read_csv("data3.csv",names=["sn","name","Class","rollno"])
# print(df)
class_12=df[df[Class]==12]
print(class_12)


   

    
