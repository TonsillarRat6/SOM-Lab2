import tkinter as tk
import random

class Printer():
    def print_ticket(self):
        printer_win = tk.Tk()
        printer_win.geometry("400x100")
        tk.Label(printer_win, text="Uw ticket wordt nu geprint, een moment alstublieft").pack(pady=20, padx=20)
        printer_win.after(random.randint(1000, 7540), lambda: printer_win.destroy())
        printer_win.mainloop()