from tkinter import Tk, ttk, constants
from db.initialize_database import initialize_database
from repositories.ledger_repository import LedgerRepository
from services.ledger_service import LedgerService

class StartView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self.d_entry = None
        self.w_entry = None

    def start(self):
        initialize_database()
        self.ledger_repository = LedgerRepository()
        label = ttk.Label(master=self._root, text="Welcome to Budget-App! :) \n \n Choose command:")
        d_label = ttk.Label(master=self._root, text="Add deposit amount and description (e.g. 100 salary:")
        self.d_entry = ttk.Entry(master=self._root)
        d_button = ttk.Button(master=self._root, text="Add deposit", command=self._d_click_handler)
        w_label = ttk.Label(master=self._root, text="Add withdrawal amount and description (e.g. 20 food:")
        self.w_entry = ttk.Entry(master=self._root)
        w_button = ttk.Button(master=self._root, text="Add withdrawal", command=self._w_click_handler)

        b_button = ttk.Button(master=self._root, text="Check budget", command=self._b_click_handler)
        l_button = ttk.Button(master=self._root, text="Check ledger", command=self._l_click_handler)
        r_button = ttk.Button(master=self._root, text="Reset ledger", command=self._r_click_handler)
        x_button = ttk.Button(master=self._root, text="Exit", command=self._x_click_handler)

        label.grid(row=0, column=0, columnspan=2, sticky=(constants.EW), padx=5, pady=5)
        d_label.grid(row=1, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self.d_entry.grid(row=2, column=0, padx=5, pady=5)
        d_button.grid(row=2, column=1)
        w_label.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self.w_entry.grid(row=4, column=0, padx=5, pady=5)
        w_button.grid(row=4, column=1)
        b_button.grid(row=5, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        l_button.grid(row=6, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        r_button.grid(row=7, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        x_button.grid(row=8, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1)

    def _l_click_handler(self):
        print(LedgerService.check_ledger(self))

    def _b_click_handler(self):
        print(LedgerService.get_balance(self))

    def _d_click_handler(self):
        value = self.d_entry.get()
        x, y = value.split(" ", maxsplit=1)
        LedgerService.deposit(self, x, y)

    def _w_click_handler(self):
        value = self.w_entry.get()
        x, y = value.split(" ", maxsplit=1)
        LedgerService.withdrawal(self, x, y)

    def _r_click_handler(self):
        LedgerService.delete_database(self)
        print("Reset complete!")

    def _x_click_handler(self):
        pass
    