import pandas as pd
df=pd.read_csv("data.csv")
# new_df=df.dropna()
# print(new_df.to_string())
# df.dropna(inplace=True)
df.fillna({"Weight":5000},inplace=True)
# print(df.to_string())
df.loc[139,"Type2"]="psYcho"
print(df.to_string())
