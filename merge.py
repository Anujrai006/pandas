import pandas as pd
df1=pd.DataFrame(
    {
        "Name":["Anuj","Ram","Sita"],
        "Id":[1,2,3]
    }
)
df2=pd.DataFrame(
    {
        "Marks":[75,45,33],
        "Id":[1,4,3]
    }
)
df=pd.merge(df1,df2,on="Id")
print(df)