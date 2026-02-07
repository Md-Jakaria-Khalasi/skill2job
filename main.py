import tkinter as tk
from ui.sidebar import Sidebar
from ui.job_circulars import JobCirculars
from ui.profile import Profile
from ui.cv import CV
from ui.skills import Skills
from ui.pathway import Pathway

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Skill2BD")
        self.geometry("1200x720")
        self.configure(bg="white")

        # Sidebar
        self.sidebar = Sidebar(self, self.show_page)
        self.sidebar.pack(side="left", fill="y")

        # Main area
        self.container = tk.Frame(self, bg="white")
        self.container.pack(side="right", fill="both", expand=True)

        self.pages = {}
        self._load_pages()
        self.show_page("JobCirculars")

    def _load_pages(self):
        self.pages["JobCirculars"] = JobCirculars(self.container)
        self.pages["MyJob"] = JobCirculars(self.container)
        self.pages["CV"] = CV(self.container)
        self.pages["Skills"] = Skills(self.container)
        self.pages["Pathway"] = Pathway(self.container)

        for page in self.pages.values():
            page.place(relwidth=1, relheight=1)

    def show_page(self, page_name):
        self.pages[page_name].tkraise()

if __name__ == "__main__":
    App().mainloop()
