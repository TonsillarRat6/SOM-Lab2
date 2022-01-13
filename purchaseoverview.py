from tkinter import messagebox

class PurchaseOverview:
	@staticmethod
	def show_overview(self, from_station, to_station, way, payment, discount, amount_tickets, price, train_class):
		#First, we make all the internal values "human readable", e.g. discount goes from 0.2, to 20, and way goes from 2, to return
		type_ticket = ["one-way", "return"]
		payment_type = ["debit card", "credit card", "cash"]
		discount *=100
		class_list = ["Second class", "First class"]
		way = type_ticket[way-1]
		payment = payment_type[payment-1]
		train_class = class_list[train_class]
		msg = (		
		f"You are buying {amount_tickets} {train_class} {way} tickets, from {from_station} station, to {to_station} Station. \n"
		f"You get a {discount}% discount, which means that you pay a total of {price} euros. \n"
		f"You chose to pay through {payment}"
		)
		return messagebox.askokcancel(title="purchase overview", message=msg)

	def cancel_payment(self):
		messagebox.showerror(title="Payment cancelled", message="You have cancelled your tickets")