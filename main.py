import tkinter as tk
from tkinter import ttk

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SimpleDashboard:
    def __init__ (self, root):
        self.root = root

        self.root.title("Simple Data Dashboard")
        self.root.geometry("1000x600")

        df = pd.read_csv('titanic.csv')

        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Column:").pack(side=tk.LEFT)
        self.column_var = tk.StringVar(value='Age')

        combo = ttk.Combobox(control_frame, textvariable=self.column_var, values=['Age', 'Fare'], width=10)
        combo.pack(side=tk.LEFT, padx=10)
        combo.bind("<<ComboboxSelected>>", self.update_chart)
    
    def update_chart(self, event=None):
        pass