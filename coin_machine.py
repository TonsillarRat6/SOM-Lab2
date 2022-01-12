from tkinter import messagebox

class IKEAMyntAtare2000:

	def starta(self):
		messagebox.showinfo(message = "Welcome to the Ikea coin-dispenser!")

	def stoppa(self):
		messagebox.showinfo(message = "Bye!")
		
	def betala(self, prijs: int):
		messagebox.showinfo(message = f"{prijs} Centen")