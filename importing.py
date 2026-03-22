import pandas as pd
df=pd.read_csv("data.csv")
# pd.options.display.max_rows=3
# pd.options.display.max_columns=3
# print(df.to_string())
# print(df.loc[135])
# for i in range(12):
#     print(df.loc[i])
# short=df[df["Height"]>1]
# print(short.to_string())
# print(df.head(8))
print(df.info())