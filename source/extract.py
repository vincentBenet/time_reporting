import tkinter as tk
from tkinter import filedialog
import os

def main():
    print("_" * 50)
    print("Start script 'extract.py'")
    root = tk.Tk()
    root.withdraw()
    dir = os.sep.join(filedialog.askdirectory().split("/"))
    print("choosen dir: " + str(dir))
    csv_list = [os.path.join(dir, f) for f in os.listdir(dir) if f.endswith(".csv") and len(f.split(" - ")) == 3]
    print("nb files detected: " + str(len(csv_list)))
    print("Finish script 'extract.py'")
    print("dir: " + str(dir))
    print("csv_list: " + str(csv_list))
    return dir, csv_list