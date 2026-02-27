import pandas as pd
df=pd.read_csv("data/raw/jobs.csv")
"""print(df.shape)
print(df.columns.tolist())
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())"""
print("\nSample job title:", df["title"][0])
print("\nSample description:", df["description"][0])
print(df.shape)