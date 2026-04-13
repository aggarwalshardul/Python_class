import pandas as pd
from sklearn.linear_model import LogisticRegression
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

df = None  # global dataframe


# -------------------- LOAD DATA --------------------
def load_data():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if file_path:
        try:
            df = pd.read_csv(file_path)
            messagebox.showinfo("Success", "Data loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


# -------------------- FEATURE ENGINEERING --------------------
def create_features():
    global df
    if df is None:
        messagebox.showerror("Error", "Load data first!")
        return

    df['KDR'] = df['Kills'] / df['Deaths'].replace(0, 1)
    df['HeadshotRatio'] = df['Headshots'] / df['Kills'].replace(0, 1)
    df['DamagePerMatch'] = df['Damage_Dealt'] / df['Matches_Played'].replace(0, 1)
    df['SurvivalTimePerMatch'] = df['Time_Survived'] / df['Matches_Played'].replace(0, 1)

    # Balanced target
    df['Win'] = (df['Wins'] > df['Wins'].median()).astype(int)

    messagebox.showinfo("Success", "Features created!")


# -------------------- TRAIN MODEL --------------------
def train_model():
    global df
    if df is None:
        messagebox.showerror("Error", "Load data first!")
        return

    try:
        X = df[['KDR', 'HeadshotRatio', 'DamagePerMatch', 'SurvivalTimePerMatch']]
        y = df['Win']

        model = LogisticRegression(max_iter=1000)
        model.fit(X, y)

        df['WinProbability'] = model.predict_proba(X)[:, 1]

        messagebox.showinfo("Success", "Model trained successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -------------------- SHOW RESULTS --------------------
def show_results():
    global df
    if df is None or 'WinProbability' not in df.columns:
        messagebox.showerror("Error", "Train model first!")
        return

    top_players = df[['Player_Name', 'WinProbability']].sort_values(by='WinProbability', ascending=False).head(10)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, top_players.to_string(index=False))


# -------------------- VISUALIZE --------------------
def visualize():
    global df
    if df is None or 'WinProbability' not in df.columns:
        messagebox.showerror("Error", "Train model first!")
        return

    plt.scatter(df['DamagePerMatch'], df['WinProbability'])
    plt.xlabel("Damage Per Match")
    plt.ylabel("Win Probability")
    plt.title("Damage vs Win Probability")
    plt.show()


# -------------------- EXPORT --------------------
def export_data():
    global df
    if df is None:
        messagebox.showerror("Error", "No data to export!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv")

    if file_path:
        df.to_csv(file_path, index=False)
        messagebox.showinfo("Success", "File exported successfully!")


# -------------------- GUI SETUP --------------------
root = tk.Tk()
root.title("PUBG Win Predictor")
root.geometry("600x500")

# Buttons
tk.Button(root, text="Load Data", command=load_data, width=20).pack(pady=5)
tk.Button(root, text="Create Features", command=create_features, width=20).pack(pady=5)
tk.Button(root, text="Train Model", command=train_model, width=20).pack(pady=5)
tk.Button(root, text="Show Top Players", command=show_results, width=20).pack(pady=5)
tk.Button(root, text="Visualize", command=visualize, width=20).pack(pady=5)
tk.Button(root, text="Export Data", command=export_data, width=20).pack(pady=5)

# Text box for output
result_text = tk.Text(root, height=15, width=70)
result_text.pack(pady=10)

root.mainloop()