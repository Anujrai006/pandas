import pandas as pd
info={
    "name":["anuj","anup"],
    "class":[11,12]
}
df=pd.DataFrame(info)
df.loc[2]=["anupa",12]
print(df)