import pandas as pd
import csv

df=pd.read_csv("dwarf_stars.csv")

df["Radius"] = 0.102763*df["Radius"]
df['Mass'] = df["Mass"].astype(float)
df["Mass"] = 0.000954588*df["Mass"]
df=df.dropna()
df.head()
df.to_csv("last.csv")