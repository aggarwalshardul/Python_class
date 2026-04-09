import pandas as pd
import matplotlib.pyplot as plt

print("===== CREATING DATAFRAME =====")
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 78]
})
print(df)


print("\n===== EXPORTING TO CSV =====")
df.to_csv('my_data.csv', index=False)
print("Data exported to my_data.csv")


print("\n===== EXPORTING TO EXCEL =====")
df.to_excel('my_data.xlsx', index=False)
print("Data exported to my_data.xlsx")


print("\n===== VERIFYING CSV BY RE-IMPORTING =====")
df_check = pd.read_csv('my_data.csv')
print(df_check)


print("\n===== VISUALIZING EXPORTED DATA =====")
df_check.plot(kind='bar', x='Name', y='Score', legend=False)
plt.xlabel("Name")
plt.ylabel("Score")
plt.title("Scores by Name")
plt.show()
