import pandas as pd

df = pd.read_csv("saas_metrics.csv")

print("SaaS Subscription Metrics")

print("\nDataset:")
print(df.head())

print("\nTotal Customers:")
print(len(df))

print("\nCustomers by Plan:")
print(df["Plan"].value_counts())

print("\nAverage Monthly Fee:")
print(df["Monthly_Fee"].mean())

print("\nActive vs Inactive Customers:")
print(df["Status"].value_counts())
