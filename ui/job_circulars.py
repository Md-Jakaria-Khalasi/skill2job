import tkinter as tk

class JobCirculars(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        # Search bar (center top)
        search = tk.Entry(
            self,
            font=("Arial", 12),
            width=50
        )
        search.pack(pady=25)

        # Cards container
        grid = tk.Frame(self, bg="white")
        grid.pack(padx=30, pady=10, fill="both", expand=True)

        cols = 4
        for i in range(12):
            card = self._job_card(grid)
            card.grid(row=i//cols, column=i%cols, padx=20, pady=20)

    def _job_card(self, parent):
        card = tk.Frame(
            parent,
            width=220,
            height=140,
            bg="white",
            highlightbackground="gray",
            highlightthickness=1
        )
        card.grid_propagate(False)

        tk.Label(card, text="Job", font=("Arial", 12, "bold"), bg="white").pack(pady=8)
        tk.Label(card, text="Post : Assistant", bg="white").pack()
        tk.Label(card, text="ABC Company", font=("Arial", 10, "bold"), bg="white").pack()

        return card
