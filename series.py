# In Pandas, a Series is a one-dimensional labeled array.
# You can think of it like a single column of data (similar to a list, but with labels called index).
import pandas as pd

data = ["marks", 100, 99, 87]
series = pd.Series(data, index=["name", "anuj", "amit", "rohan"])
print(series)
