import pandas as pd
#aggregate in pandas:Aggregation in pandas is the process of summarizing data 
# using functions like sum(), mean(), min(), max(), and count()
df=pd.read_csv("data1.csv")
#For Whole data
avg_data=df.mean(numeric_only=True)
# print(avg_data)
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
print(df.count())
