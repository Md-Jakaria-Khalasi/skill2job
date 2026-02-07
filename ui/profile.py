import tkinter as tk

class Profile(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Profile Page", font=("Arial", 18), bg="white").pack(pady=40)
