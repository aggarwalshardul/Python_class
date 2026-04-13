import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from tkinter import filedialog, messagebox

def load_data():
    try:
        df = pd.read_csv('Pubg_Stats.csv')
        return df
    except FileNotFoundError:
        print("Error: Pubg_Stats.csv not found.")
        return None

def create_features(df):
    df = df.copy()

    df['KDR'] = df['Kills'] / df['Deaths'].replace(0, 1)
    df['HeadshotRatio'] = df['Headshots'] / df['Kills'].replace(0, 1)
    df['DamagePerMatch'] = df['Damage_Dealt'] / df['Matches_Played'].replace(0, 1)
    df['SurvivalTimePerMatch'] = df['Time_Survived'] / df['Matches_Played'].replace(0, 1)

    # ✅ FIXED TARGET
    df['Win'] = (df['Wins'] > df['Wins'].median()).astype(int)

    return df
def calculate_win_probabilities(df):
    X = df[['KDR', 'HeadshotRatio', 'DamagePerMatch', 'SurvivalTimePerMatch']]
    y = df['Win']

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    probabilities = model.predict_proba(X)[:, 1]

    df['WinProbability'] = probabilities
    return df

def visualize_data(df):
    plt.scatter(df['DamagePerMatch'], df['WinProbability'])
    plt.xlabel('Damage Per Match')
    plt.ylabel('Win Probability')
    plt.title('Damage vs Win Probability')
    plt.show()

def export_data(df):
    file_path = filedialog.asksaveasfilename(
        title="Save PUBG Data",
        filetypes=[("CSV Files", "*.csv")]
    )

    if file_path:
        try:
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Success", f"Data saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    df = load_data()

    if df is not None:
        df = create_features(df)
        df = calculate_win_probabilities(df)

        print(df[['Player_Name', 'WinProbability']].head())

        visualize_data(df)
