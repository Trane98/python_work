import pandas as pd
df=pd.read_csv(r"C:\Program Files (x86)\python_work\P0 projekt\Mean_ALLE.csv", delimiter=";")
df_dropna = df.dropna()
df_dropna.to_csv("Mean_klar.csv")
