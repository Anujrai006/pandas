import pandas as pd
info={
    "name":["anuj","anupa","anup"],
    "class":[11,11,12],
    "marks":[22,23,22]
}
df=pd.DataFrame(info)
df.loc[3]=["anuja",12,22]
grouped=df.groupby("class")["marks"].sum()
print(grouped)

