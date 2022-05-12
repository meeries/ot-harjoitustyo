from tkinter import Tk, ttk, constants, messagebox
from repositories.ledger_repository import LedgerRepository
from services.ledger_service import LedgerService
import re

class StartView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self.d_entry = None
        self.w_entry = None

    def start(self):
        """Lisää ikkunan ja näyttää siinä tarvittavat napit ja labelit jne.
        """
        self.ledger_repository = LedgerRepository()
        label = ttk.Label(master=self._root, text="Welcome to Budget-App! :) \n \n Choose command:")
        d_label = ttk.Label(master=self._root, text="Add deposit amount and description separated by a comma or a space (e.g. 100, salary):")
        self.d_entry = ttk.Entry(master=self._root)
        d_button = ttk.Button(master=self._root, text="Add deposit", command=self._d_click_handler)
        w_label = ttk.Label(master=self._root, text="Add withdrawal amount and description separated by a comma or a space (e.g. 20 food):")
        self.w_entry = ttk.Entry(master=self._root)
        w_button = ttk.Button(master=self._root, text="Add withdrawal", command=self._w_click_handler)

        b_button = ttk.Button(master=self._root, text="Check budget", command=self._b_click_handler)
        l_button = ttk.Button(master=self._root, text="Check ledger", command=self._l_click_handler)
        r_button = ttk.Button(master=self._root, text="Reset ledger", command=self._r_click_handler)

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

        self._root.grid_columnconfigure(1, weight=1)

    def _l_click_handler(self):
        """Kutsuu servicestä senhetkisen kirjanpidon palauttavaa metodia ja näyttää uudessa ikkunassa senhetkisen kirjanpidon
        """
        a = LedgerService.check_ledger(self)
        text = f"Your current ledger: {a}"
        messagebox.showinfo(" ", text)

    def _b_click_handler(self):
        """Kutsuu servicestä senhetkisen budjetin palauttavaa metodia ja näyttää uudessa ikkunassa senhetkisen budjetin.
        """
        b = LedgerService.get_balance(self)
        text = f"Your current budget is: {b}"
        messagebox.showinfo(" ", text)

    def _d_click_handler(self):
        """Jakaa annetun arvon summaan ja sen kuvaukseen välilyönnistä tai pilkusta.
        Kutsuu serviceä joka varmistaa, että summa on numero, varmistaa, että se on positiivinen ja lisää talletuksen budjettiin ja kirjanpitoon.
        Näyttää varmistusviestin tai tarvittaessa varoitusviestin.
        (Oli pakko lisätä tämä sovelluslogiikan pätkä käyttöliittymään, koska se ei muuten toiminut.)
        """
        value = self.d_entry.get()
        x, y = re.split("\s|,", value, maxsplit=1)
        if LedgerService.is_it_a_number(self,x) is False:
            messagebox.showerror(" ", "Add amount as a number.")
        else:
            if int(x) > 0:
                LedgerService.deposit(self, x, y)
                messagebox.showinfo(" ", "Deposit added!")
            else:
                messagebox.showerror(" ", "Please insert a positive number")

    def _w_click_handler(self):
        """Kutsuu serviceä joka varmistaa, että summa on numero, varmistaa, että se on positiivinen ja että
        budjetissa on riittävästi rahaa nostoon. Jos on, lisää noston budjettiin ja kirjanpitoon.
        Näyttää varmistusviestin tai varoitusviestin.
        (Oli pakko lisätä tämä sovelluslogiikan pätkä käyttöliittymään, koska se ei muuten toiminut.)
        """
        value = self.w_entry.get()
        x, y = re.split("\s|,", value, maxsplit=1)
        if LedgerService.is_it_a_number(self,x) is False:
            messagebox.showerror(" ", "Add amount as a number.")
        else:
            if int(x) > 0:
                if LedgerService.get_balance(self) - int(x) > 0:
                    LedgerService.withdrawal(self, x, y)
                    messagebox.showinfo(" ", "Withdrawal added!")
                else:
                    messagebox.showerror(" ", "Not enough balance for withdrawal.")
            else:
                messagebox.showerror(" ", "Please insert a positive number")

    def _r_click_handler(self):
        """"Kutsuu servicen tietokannan tyhjentävää metodia ja näyttää varmistusviestin.
        """
        LedgerService.delete_database(self)
        messagebox.showinfo(" ", "Reset complete!")
