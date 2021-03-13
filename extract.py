import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

dir = os.sep.join(filedialog.askdirectory().split("/"))

csv_list = [os.path.join(dir, f) for f in os.listdir(dir) if f.endswith(".csv")]

