from tkinter import Tk
from start_view import StartView
from ui.deposit_view import DepositView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()
    
    def _show_deposit_view(self):
        self._current_view = DepositView(
            self._root,
        )
        self._current_view.pack()

    def _show_start_view(self):
        self._current_view = StartView(
            self._current_view.destroy(),
            self._root
        )
        self._current_view.pack()

window = Tk()
window.title("Budget-app")

ui = UI(window)
ui.start()

window.mainloop()