import tkinter as tk

class Skills(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        tk.Label(
            self,
            text="My Skills",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=40)
