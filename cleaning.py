import pandas as pd
df=pd.read_csv("data.csv")
##Removing Irelevant data
# df=df.drop(columns=["Legendary"])
#handle misiing data
# df=df.dropna(subset=["Type2"])
# df=df.fillna({"Type2":"None"})
# print(df.to_string())
#FIX INCONSISTENT VALUES
df["Type1"]=df["Type1"].replace({
    "Grass":"GRASS"
})
#STANDARIZE DATA
df["Name"]=df["Name"].str.lower()
df["Legendary"]=df["Legendary"].astype(bool)
df=df.drop_duplicates()
print(df)

