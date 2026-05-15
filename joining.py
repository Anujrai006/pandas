import pandas as pd
df1=pd.DataFrame(
    {
        "Name":["Anuj","Ram","Hari"],
        "class":[11,12,10]
    },index=[1,2,3]
)
df2=pd.DataFrame(
    {
        "Age":[17,18,15]
    },index=[2,3,4]
)
# df=df1.join(df2)
df=pd.concat([df1,df2],axis=1)
print(df)