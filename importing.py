import pandas as pd
data=pd.read_csv("data.csv")
pd.options.display.max_rows=3
pd.options.display.max_columns=3
# print(data.to_string())
# print(data.loc[135])
# for i in range(12):
#     print(data.loc[i])
# short=data[data["Height"]>1]
# print(short.to_string())
print(data)