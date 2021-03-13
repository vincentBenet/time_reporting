import tkinter as tk
from tkinter import filedialog
import os

def main():
    root = tk.Tk()
    root.withdraw()
    dir = os.sep.join(filedialog.askdirectory().split("/"))
    # print("choosen dir: " + str(dir))
    csv_list = [os.path.join(dir, f) for f in os.listdir(dir) if f.endswith(".csv") and len(f.split(" - ")) == 3]
    # print("nb files: " + str(len(csv_list)))
    return dir, csv_list