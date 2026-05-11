import pandas as pd
df=pd.read_csv("duplicate.csv")
df.drop_duplicates(inplace=True)
print(df.to_string())
print(df.duplicated())