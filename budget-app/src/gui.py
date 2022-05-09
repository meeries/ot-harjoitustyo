from tkinter import Tk
from ui.start_view import StartView

window = Tk()
window.title("Budget-app")


ui = StartView(window)
ui.start()
window.mainloop()
