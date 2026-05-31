import pandas as pd
df=pd.DataFrame({
    "Age":[11,12,13,14],
})
def square(x):
    return x**2
df["square"]=df["Age"].apply(square)
print(df.to_string())