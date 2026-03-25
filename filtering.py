import pandas as pd
df=pd.read_csv("data.csv")
small_pokemon=df[(df["Height"]<1) & (df["Height"]>0.5)] 
print(small_pokemon)