# In Pandas, a Series is a one-dimensional labeled array.
# You can think of it like a single column of data (similar to a list, but with labels called index).
import pandas as pd

data = [100, 99, 87]
series = pd.Series(data, index=[ "anuj", "amit", "rohan"])
# print(series)
series.loc["rohan"]=99
# print(series[series > 99])
# print(series.loc["anuj"])
calories={"Day-1":1200,"Day-2":1400,"Day-3":1250}
series1=pd.Series(calories) 
series1.loc["Day-2"]=1700

print(series1.loc["Day-2"])
print(series1[series1 < 1300])
# print(series1)