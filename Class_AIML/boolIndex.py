import pandas as pd

print("===== CREATING DATAFRAME =====")
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
})
print(df)


print("\n===== FILTERING BY A SINGLE CONDITION =====")
# Filter rows where column A is greater than 2
df_single = df[df['A'] > 2]
print(df_single)


print("\n===== FILTERING BY MULTIPLE CONDITIONS (AND) =====")
# Filter rows where A > 2 and B < 4
df_multiple = df[(df['A'] > 2) & (df['B'] < 4)]
print(df_multiple)


print("\n===== FILTERING USING isin() FUNCTION =====")
# Filter rows where A is either 1 or 3
df_isin = df[df['A'].isin([1, 3])]
print(df_isin)
