import pandas as pd
from sklearn.linear_model import LogisticRegression
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


df = None
model = None

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

    df['Win'] = (df['Wins'] > df['Wins'].median()).astype(int)

    messagebox.showinfo("Success", "Features created!")


# -------------------- TRAIN MODEL --------------------
def train_model():
    global df, model

    if df is None:
        messagebox.showerror("Error", "Load data first!")
        return

    try:
        X = df[['KDR', 'HeadshotRatio', 'DamagePerMatch', 'SurvivalTimePerMatch']]
        y = df['Win']

        model = LogisticRegression(max_iter=1000)
        model.fit(X, y)

        df['WinProbability'] = model.predict_proba(X)[:, 1]

        messagebox.showinfo("Success", "Model trained!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -------------------- PREDICT NEW PLAYER --------------------
def predict_player():
    global model

    if model is None:
        messagebox.showerror("Error", "Train model first!")
        return

    try:
        kills = float(entry_kills.get())
        deaths = float(entry_deaths.get())
        headshots = float(entry_headshots.get())
        damage = float(entry_damage.get())
        matches = float(entry_matches.get())
        time_survived = float(entry_time.get())

        # Features
        kdr = kills / (deaths if deaths != 0 else 1)
        hs_ratio = headshots / (kills if kills != 0 else 1)
        dmg_per_match = damage / (matches if matches != 0 else 1)
        survival_per_match = time_survived / (matches if matches != 0 else 1)

        X_new = pd.DataFrame([{
            'KDR': kdr,
            'HeadshotRatio': hs_ratio,
            'DamagePerMatch': dmg_per_match,
            'SurvivalTimePerMatch': survival_per_match
        }])

        prob = model.predict_proba(X_new)[0][1]


        result_label.config(text=f"Win Probability: {prob:.2f}", fg="#00ffcc")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -------------------- GUI --------------------
root = tk.Tk()
root.title("Win Predictor Pro")
root.geometry("700x600")
root.configure(bg="#1e1e2f")

title = tk.Label(root, text=" Win Predictor", font=("Arial", 20, "bold"), bg="#060657", fg="#00ffcc")
title.pack(pady=10)

# Buttons
btn_style = {"width": 20, "bg": "#2d2d44", "fg": "white", "bd": 0}

tk.Button(root, text="Load Data", command=load_data, **btn_style).pack(pady=5)
tk.Button(root, text="Create Features", command=create_features, **btn_style).pack(pady=5)
tk.Button(root, text="Train Model", command=train_model, **btn_style).pack(pady=5)

# -------------------- INPUT SECTION --------------------
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

def make_entry(label_text):
    tk.Label(frame, text=label_text, bg="#1e1e2f", fg="white").pack()
    entry = tk.Entry(frame)
    entry.pack()
    return entry

entry_kills = make_entry("Kills")
entry_deaths = make_entry("Deaths")
entry_headshots = make_entry("Headshots")
entry_damage = make_entry("Total Damage")
entry_matches = make_entry("Matches Played")
entry_time = make_entry("Time Survived")

tk.Button(root, text="Predict Player", command=predict_player, bg="#00ffcc", fg="black", width=20).pack(pady=10)

result_label = tk.Label(root, text="Win Probability: --", font=("Arial", 14), bg="#1e1e2f", fg="white")
result_label.pack(pady=10)

root.mainloop()