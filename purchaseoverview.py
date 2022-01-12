from tkinter import messagebox

class PurchaseOverview:

	def show_overview(self, from_station, to_station, way, discount, payment, amount_tickets, price):
		#First, we make all the internal values "human readable", e.g. discount goes from 0.2, to 20, and way goes from 2, to return
		type_ticket = ["single", "return"]
		payment_type = ["debit card", "credit card", "cash"]
		discount *=100
		way = type_ticket[way-1]
		payment = payment_type[payment-1]
		msg = (		
		f"You are buying {amount_tickets} {way} tickets, from {from_station} station, to {to_station}, station. \n"
		f"You get a {discount}% discount, which means that you pay a total of {price} euros. \n"
		f"You chose to pay through {payment}"
		)
		return messagebox.askokcancel(title="purchase overview", message=msg)

	def cancel_payment(self):
		messagebox.showerror(title="Payment cancelled", message="You have cancelled your tickets")