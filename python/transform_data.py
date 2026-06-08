import pandas as pd

df = pd.read_csv("../datasets/sales.csv")

df.columns = df.columns.str.replace(" ", "_")

df.drop_duplicates(inplace=True)

df.to_csv("../datasets/clean_sales.csv", index=False)

print("Data cleaned successfully")
