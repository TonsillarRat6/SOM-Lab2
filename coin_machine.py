from tkinter import messagebox

class CoinMachine:

	def start_payment(self):
		messagebox.showinfo(message = "Welcome to the Ikea coin-dispenser!")

	def stop_payment(self):
		messagebox.showinfo(message = "Bye!")
		
	def coin_machine_payment(self, prijs: int):
		messagebox.showinfo(message = f"{prijs} euro")