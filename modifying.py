import pandas as pd
Studnets={
    "Name":["anuj","bibash","chandra","dipak"],
    "Age":[12,13,14,19],
    "Physics":[10,11,23,22],
    "Chemistry":[21,22,12,29]

}
df=pd.DataFrame(Studnets)
df["height"]=[170,180,153,123]
df.rename(columns={"height":"Height"},inplace=True)

print(df)