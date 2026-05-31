import pandas as pd
df=pd.DataFrame({
    "Age":["11","12","13"],
})
df["Age"]=df["Age"].astype(float)
print(df.dtypes)