import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from analysis import load_data, calculate_win_probabilities, visualize_data, export_data


class EsportsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Esports Win Prediction Analysis")

        self.df = None  # ✅ store dataframe

        # --- Buttons ---
        tk.Button(root, text="Load Data", command=self.load_data).pack(pady=10)
        tk.Button(root, text="Run Analysis", command=self.run_analysis).pack(pady=10)
        tk.Button(root, text="Export Data", command=self.export_data).pack(pady=10)

        # --- Text Area ---
        self.results_text = tk.Text(root, height=15, width=80)
        self.results_text.pack(pady=10)

        # --- Plot Area ---
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

    def load_data(self):
        self.df = load_data()

        if self.df is not None:
            self.results_text.delete("1.0", tk.END)
            self.results_text.insert(tk.END, "Data loaded successfully!\n")

    def run_analysis(self):
        if self.df is None:
            messagebox.showerror("Error", "Please load data first!")
            return

        win_probabilities = calculate_win_probabilities(self.df)

        self.results_text.delete("1.0", tk.END)

        for i, prob in enumerate(win_probabilities):
            self.results_text.insert(tk.END, f"Player {i+1}: {prob:.2f}\n")

        # --- Plot inside GUI ---
        self.ax.clear()
        self.ax.scatter(self.df['CSPerMinute'], self.df['Win'])
        self.ax.set_xlabel('CS Per Minute')
        self.ax.set_ylabel('Win')
        self.ax.set_title('CS Per Minute vs Win')

        self.canvas.draw()

    def export_data(self):
        if self.df is None:
            messagebox.showerror("Error", "No data to export!")
            return

        export_data(self.df)


# Run app
if __name__ == '__main__':
    root = tk.Tk()
    app = EsportsApp(root)
    root.mainloop()
    