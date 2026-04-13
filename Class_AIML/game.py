import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("Pubg_Stats.csv")


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

print("Columns:", df.columns)


df = df.dropna()

df['win_percentage'] = df['wins'] / df['matches_played']

X = df[['kills', 'damage_dealt', 'distance_traveled', 'time_survived']]
y = df['win_percentage']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


model = RandomForestRegressor()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("\nModel Accuracy:", accuracy)

print("\nEnter your player stats:")

kills = float(input("Kills: "))
damage = float(input("Damage Dealt: "))
distance = float(input("Distance Traveled: "))
time = float(input("Time Survived: "))

new_player = pd.DataFrame([[kills, damage, distance, time]],
                          columns=['kills', 'damage_dealt', 'distance_traveled', 'time_survived'])


prediction = model.predict(new_player)[0]

print("\n🎯 Predicted Win Probability:", round(prediction * 100, 2), "%")


# Graph 1: Kills vs Win %
plt.figure()
plt.scatter(df['kills'], df['win_percentage'])
plt.xlabel("Kills")
plt.ylabel("Win Percentage")
plt.title("Kills vs Win Percentage")
plt.show()

# Graph 2: Damage vs Win %
plt.figure()
plt.scatter(df['damage_dealt'], df['win_percentage'])
plt.xlabel("Damage Dealt")
plt.ylabel("Win Percentage")
plt.title("Damage vs Win Percentage")
plt.show()

# Graph 3: Distribution of Win %
plt.figure()
plt.hist(df['win_percentage'], bins=20)
plt.xlabel("Win Percentage")
plt.ylabel("Frequency")
plt.title("Distribution of Win Percentage")
plt.show()