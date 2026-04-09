import pandas as pd

print("===== CREATING DATAFRAME =====")
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50]
})
print(df)


print("\n===== GROUPING DATA =====")
grouped = df.groupby('Category')
print(grouped)


print("\n===== AGGREGATION: SUM =====")
print(df.groupby('Category')['Value'].sum())


print("\n===== AGGREGATION: MEAN =====")
print(df.groupby('Category')['Value'].mean())


print("\n===== MULTIPLE AGGREGATIONS =====")
print(df.groupby('Category')['Value'].agg(['sum', 'mean', 'count']))
