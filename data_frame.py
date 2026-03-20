import pandas as pd
data={
    "name":["anuj","hari","shyam"],
    "class":[11,12,13],
}
df=pd.DataFrame(data,index=["student 1","student 2","student 3"])
# print(df.loc["student 1"])
df["age"]=[15,26,27]
# print(df)
new_df=pd.DataFrame([{"name":"anujaa","class":11,"age":16},{"name":"anita","class":11,"age":26}],index=["student 4","student 5"])
df=pd.concat([df,new_df])
print(df)
