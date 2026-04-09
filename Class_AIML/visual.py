import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
print(df.head)
print(df.describe())
df.plot(x='Quantity', y='UnitPrice', kind='line')
plt.show()
print(df.isnull().sum())
df_clean = df.dropna()
print(df_clean)
# df = df.set_index('A')
# print(df)