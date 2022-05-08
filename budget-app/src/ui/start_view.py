from tkinter import Tk, ttk, constants
window = Tk()
window.title("Budget-app")


class StartView:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Welcome to Budget-App! :) \n \n Choose command:")
        d_button = ttk.Button(master=self._root, text="Deposit")
        w_button = ttk.Button(master=self._root, text="Withdrawal")
        b_button = ttk.Button(master=self._root, text="Check budget")
        l_button = ttk.Button(master=self._root, text="Check ledger")
        r_button = ttk.Button(master=self._root, text="Reset ledger")
        x_button = ttk.Button(master=self._root, text="Exit")

        label.grid(row=0, column=0, columnspan=2, sticky=(constants.EW), padx=5, pady=5)
        d_button.grid(row=1, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        w_button.grid(row=2, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        b_button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        l_button.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        r_button.grid(row=5, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        x_button.grid(row=6, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1)

    def _click_handler(self):
        pass
        

window = Tk()
window.title("Budget-app")

ui = StartView(window)
ui.start()
window.mainloop()