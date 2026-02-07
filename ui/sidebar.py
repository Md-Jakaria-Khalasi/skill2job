import tkinter as tk
from pydoc import pager
from struct import pack
from textwrap import fill


class Sidebar(tk.Frame):
    def __init__(self, parent, callback):
        super().__init__(parent, width=230, bg="#e58b8b")
        self.callback = callback
        self.pack_propagate(False)

        # Logo
        tk.Label(
            self,
            text="Skill2BD",
            bg="#6b4c4c",
            fg="white",
            font=("Arial", 16, "bold"),
            pady=20
        ).pack(fill="x", padx=10, pady=10)

        tk.Button(
            self,
            text="Job Circulars",
            bg="#d9d9d9",
            font=("Arial", 12),
            command=lambda: self.callback("JobCirculars")
        ).pack(side="left",fill="x", padx=20, pady=20)

        self._menu("Job Circulars", "JobCirculars")
        self._menu("My Job", "MyJob")
        self._menu("CV", "CV")
        self._menu("My Skils", "Skills")
        self._menu("My Pathway", "Pathway")

        # Bottom profile
        tk.Button(
            self,
            text="Profile",
            bg="#d9d9d9",
            font=("Arial", 12),
            command=lambda: self.callback("Profile")
        ).pack(side="bottom", fill="x", padx=20, pady=20)

    def _menu(self, text, page):
        tk.Button(
            self,
            text=text,
            anchor="w",
            bg="#e58b8b",
            bd=0,
            font=("Arial", 12),
            command=lambda: self.callback(page)
        ).pack(fill="x", padx=20, pady=6)
