import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tips.csv')
print(df)

print("\nNumber of samples (rows):", df.shape[0])
print("Number of features (columns):", df.shape[1])
print(df.isnull().sum())
print(df[['total_bill','tip','size']].describe())
df['tip_percent'] = (df['tip'] / df['total_bill']) * 100

plt.boxplot(df['tip_percent'])
plt.show()

# top_10 = df.sort_values(by='tip_percent', ascending=False).head(10)
# print(top_10)

# print(df.groupby('day')['tip'].mean())
# print(df.groupby('smoker')['tip_percent'].mean())
# # plt.hist(df['total_bill'], bins=20)
# # plt.show()
# avg_tip_byDay = df.groupby('day')['tip'].mean()
# print(avg_tip_byDay)
# plt.scatter(df['total_bill'], df['tip'])
# plt.xlabel('Total Bill')
# plt.ylabel('Tip')
# plt.title('Scatter Plot: Total Bill vs Tip')
# plt.show()

# avg_tip_by_size = df.groupby('size')['tip'].mean()
# plt.plot(avg_tip_by_size.index, avg_tip_by_size.values, marker='o')
# plt.xlabel('Group Size')
# plt.ylabel('Average Tip')
# plt.title('Average Tip by Group Size')
# plt.grid(True)
# plt.show()


