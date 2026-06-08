import pandas as pd

df = pd.read_csv("../datasets/sales.csv")

# Standardize columns
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna("Unknown", inplace=True)

# Save cleaned file
df.to_csv("../datasets/clean_sales.csv", index=False)

print("ETL Completed Successfully")
