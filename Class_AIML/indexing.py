import pandas as pd

print("DEFAULT INDEXING ")
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
print(df)


print("\n SETTING A CUSTOM INDEX ")
df_custom = df.set_index('A')
print(df_custom)


print("\nRESETTING THE INDEX ")
df_reset = df_custom.reset_index()
print(df_reset)


print("\n MULTIINDEX (HIERARCHICAL INDEXING) ")
df_multi = pd.DataFrame({
    'Class': ['FY', 'FY', 'SY', 'SY'],
    'Roll_No': [1, 2, 1, 2],
    'Marks': [78, 85, 88, 90]
})
print(df_multi)
df_multi = df_multi.set_index(['Class', 'Roll_No'])
print(df_multi)