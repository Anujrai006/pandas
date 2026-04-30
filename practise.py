import pandas as pd
# df=pd.read_csv("data.csv")
dict={
    "name":"anuj",
    "age":17,
    "class":11
}
df=pd.Series(dict)
print(df)