import pandas as pd
students=[{'name':"anuj","class":11,"roll":1},{'name':"anusha","class":12,"roll":11},
          {'name':"anuja","class":None ,"roll":10},{'name':"sweta","class":None,"roll":2}]
df=pd.DataFrame(students)
new=df.drop(columns=["class"],axis=1)
print(new)
# df.loc[df["name"]=="anuja","class"]=9
# df.loc[df["name"]=="sweta","class"]=11
# print(df)
