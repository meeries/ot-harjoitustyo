from tkinter import Tk, ttk
window = Tk()
window.title("Budget-app")


class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Welcome to Budget-App! :) \n choose command:")
        d_button = ttk.Button(master=self._root, text="Deposit")
        w_button = ttk.Button(master=self._root, text="Withdrawal")
        b_button = ttk.Button(master=self._root, text="Check budget")
        l_button = ttk.Button(master=self._root, text="Check ledger")

        label.grid(row=0, column=0, columnspan=2)
        d_button.grid(row=1, column=0)
        w_button.grid(row=1, column=2)
        b_button.grid(row=1, column=4)
        l_button.grid(row=1, column=6)


window = Tk()
window.title("Budget-app")

ui = UI(window)
ui.start()
window.mainloop()
