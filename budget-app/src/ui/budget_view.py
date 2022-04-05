from tkinter import Tk, ttk
from repositories.budget_repository import Budget
window = Tk()
window.title("Budget-app")

class StartScreen:
    def __init__(self, root):
        self.root = root

    def start_screen(self):
        start_label = ttk.Label(self.root, text=":)")
        start_label.grid(row=0, column=0, columnspan=2)


startscreen = StartScreen(window)
startscreen.start_screen()
window.mainloop()