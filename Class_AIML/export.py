import pandas as pd

print("===== CREATING DATAFRAME =====")
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Score': [85, 90, 85, None],
    'Date': ['2024-01-10', '2024-01-11', '2024-01-10', '2024-01-12'],
    'Remarks': ['Good', 'Excellent', 'Good', None]
})
print(df)


print("\n===== CLEANING DATA =====")
df = df.drop_duplicates().reset_index(drop=True)
print(df)


print("\n===== ENSURING CONSISTENT DATA TYPES =====")
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes)


# print("\n===== HANDLING MISSING VALUES =====")
# df = df.fillna('N/A')
# print(df)


# print("\n===== SELECTING RELEVANT COLUMNS FOR EXPORT =====")
# df_export = df[['Name', 'Score', 'Date']]
# print(df_export)
