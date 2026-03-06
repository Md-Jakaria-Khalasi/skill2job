import tkinter as tk
from tkinter import filedialog
import json
import os

FILE = "cv_data.json"


# ================= LOAD DATA =================
def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


# ================= SAVE DATA =================
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


class CV(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="white")

        self.data = load_data()

        # ===== TOP BUTTON =====
        self.top = tk.Frame(self, bg="white")
        self.top.pack(fill="x", pady=10)

        tk.Button(
            self.top,
            text="View CV",
            command=self.view_cv,
            bg="#4CAF50",
            fg="white"
        ).pack(side="left", padx=10)

        tk.Button(
            self.top,
            text="Edit CV",
            command=self.edit_cv,
            bg="#2196F3",
            fg="white"
        ).pack(side="left")

        # ===== MAIN CONTAINER =====
        self.container = tk.Frame(self, bg="white")
        self.container.pack(fill="both", expand=True)

        self.view_cv()

    # ================= CLEAR =================
    def clear(self):
        for w in self.container.winfo_children():
            w.destroy()

    # ================= VIEW CV =================
    def view_cv(self):

        self.clear()

        main = tk.Frame(self.container, bg="#3c4657")
        main.pack(fill="x")

        header = tk.Frame(main, bg="#3c4657")
        header.pack(pady=30)

        # ===== PHOTO =====
        if self.data.get("photo") and os.path.exists(self.data["photo"]):
            img = tk.PhotoImage(file=self.data["photo"])
            img = img.subsample(4, 4)

            photo = tk.Label(header, image=img, bg="#3c4657")
            photo.image = img
            photo.pack(side="left", padx=40)

        text = tk.Frame(header, bg="#3c4657")
        text.pack(side="left")

        tk.Label(
            text,
            text=self.data.get("name", ""),
            font=("Arial", 28, "bold"),
            fg="white",
            bg="#3c4657"
        ).pack(anchor="w")

        tk.Label(
            text,
            text=self.data.get("title", ""),
            font=("Arial", 16),
            fg="white",
            bg="#3c4657"
        ).pack(anchor="w")

        body = tk.Frame(self.container, bg="white")
        body.pack(fill="both", expand=True)

        left = tk.Frame(body, bg="white", width=300)
        left.pack(side="left", fill="y", padx=20, pady=20)

        divider = tk.Frame(body, width=2, bg="gray")
        divider.pack(side="left", fill="y")

        right = tk.Frame(body, bg="white")
        right.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # ================= LEFT =================

        tk.Label(left, text="CONTACT", font=("Arial", 14, "bold")).pack(anchor="w")

        tk.Label(
            left,
            text="📞 " + self.data.get("phone", ""),
            font=("Arial", 11)
        ).pack(anchor="w")

        tk.Label(
            left,
            text="✉️ " + self.data.get("email", ""),
            font=("Arial", 11)
        ).pack(anchor="w")

        tk.Label(
            left,
            text="🏠 " + self.data.get("address", ""),
            font=("Arial", 11),
            wraplength=250
        ).pack(anchor="w")

        tk.Label(left, text="").pack()

        tk.Label(left, text="EDUCATION", font=("Arial", 14, "bold")).pack(anchor="w")
        tk.Label(
            left,
            text=self.data.get("education", ""),
            justify="left",
            wraplength=250
        ).pack(anchor="w")

        tk.Label(left, text="").pack()

        tk.Label(left, text="SKILLS", font=("Arial", 14, "bold")).pack(anchor="w")
        tk.Label(
            left,
            text=self.data.get("skills", ""),
            justify="left",
            wraplength=250
        ).pack(anchor="w")

        tk.Label(left, text="").pack()

        tk.Label(left, text="AWARDS", font=("Arial", 14, "bold")).pack(anchor="w")
        tk.Label(left, text=self.data.get("awards", "")).pack(anchor="w")

        # ================= RIGHT =================

        tk.Label(right, text="PROFILE", font=("Arial", 14, "bold")).pack(anchor="w")
        tk.Label(
            right,
            text=self.data.get("profile", ""),
            wraplength=500
        ).pack(anchor="w")

        tk.Label(right, text="").pack()

        tk.Label(right, text="WORK EXPERIENCE", font=("Arial", 14, "bold")).pack(anchor="w")
        tk.Label(
            right,
            text=self.data.get("experience", ""),
            justify="left",
            wraplength=500
        ).pack(anchor="w")

        tk.Label(right, text="").pack()

        tk.Label(right, text="REFERENCES", font=("Arial", 14, "bold")).pack(anchor="w")
        tk.Label(right, text=self.data.get("references", "")).pack(anchor="w")

    # ================= EDIT CV =================
    def edit_cv(self):

        self.clear()

        frame = tk.Frame(self.container, bg="white")
        frame.pack(pady=20)

        self.entries = {}

        fields = [
            "name", "title", "phone", "email", "address",
            "profile", "education", "skills",
            "experience", "awards", "references"
        ]

        r = 0

        for f in fields:

            tk.Label(
                frame,
                text=f.capitalize(),
                bg="white"
            ).grid(row=r, column=0, sticky="w")

            e = tk.Entry(frame, width=50)

            e.grid(row=r, column=1, pady=5)

            e.insert(0, self.data.get(f, ""))

            self.entries[f] = e

            r += 1

        tk.Button(
            frame,
            text="Upload Photo",
            command=self.upload
        ).grid(row=r, column=0)

        tk.Button(
            frame,
            text="Save",
            bg="#4CAF50",
            fg="white",
            command=self.save
        ).grid(row=r, column=1)

    # ================= PHOTO =================
    def upload(self):

        path = filedialog.askopenfilename()

        if path:
            self.data["photo"] = path

    # ================= SAVE =================
    def save(self):

        for k, e in self.entries.items():
            self.data[k] = e.get()

        save_data(self.data)

        self.view_cv()


# ================= RUN APP =================
if __name__ == "__main__":

    root = tk.Tk()

    root.title("CV Builder")

    root.geometry("1200x700")

    cv = CV(root)

    cv.pack(fill="both", expand=True)

    root.mainloop()