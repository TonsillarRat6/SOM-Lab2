from calendar import weekday
from pickle import TRUE
import tkinter as tk
from tariefeenheden import Tariefeenheden
from pricing_table import PricingTable
from creditcard import CreditCard
from debitcard import DebitCard
from coin_machine import CoinMachine
from ui_info import UIPayment, UIClass, UITicketAmount, UIWay, UIDiscount, UIPayment, UIInfo
from purchaseoverview import PurchaseOverview
from printer import Printer

class UI(tk.Frame):

	def __init__(self, master):
		tk.Frame.__init__(self, master)
		self.widgets()

	def get_tariefeenheden(self, info:UIInfo):
		tariefeenheden: int = Tariefeenheden.get_tariefeenheden(info.from_station, info.to_station)
		return tariefeenheden

	def get_class(self, info: UIInfo):
		train_class = 0
		if info.travel_class == UIClass.FirstClass:
			train_class = 1
		return train_class

	def get_discount(self, info: UIInfo):
		discount = 0
		if info.discount == UIDiscount.TwentyDiscount:
			discount = 0.2
		elif info.discount == UIDiscount.FortyDiscount:
			discount = 0.4
		return discount

	def get_ticket_type(self, info: UIInfo):
		way = 1
		if info.way == UIWay.Return:
			way = 2
		return way

	def calc_price(self, way, tariefeenheden, discount, train_class, amount_tickets):
		price: float = PricingTable.get_price (tariefeenheden, discount, train_class, amount_tickets)
		price *= way
		return round(price,2)

	def credit_card_price(self, info: UIInfo, price):
		# add 50 cents if paying with credit card
		if info.payment == UIPayment.CreditCard:
			price += 0.50
		return price
		
	def show_overview(self, info: UIInfo, discount, price, amount_tickets, train_class):
		overview = PurchaseOverview()
		if overview.show_overview(info.from_station, info.to_station, info.way, info.payment, discount, amount_tickets, price, train_class):
			return True
		else:
			return False

		
	def do_payment(self, info: UIInfo, price):
		if info.payment == UIPayment.CreditCard:
			c = CreditCard()
			c.connect()
			ccid: int = c.begin_transaction(round(price, 2))
			c.end_transaction(ccid)
			c.disconnect()
		elif info.payment == UIPayment.DebitCard:
			d = DebitCard()
			d.connect()
			dcid: int = d.begin_transaction(round(price, 2))
			d.end_transaction(dcid)
			d.disconnect()
		elif info.payment == UIPayment.Cash:
			coin = CoinMachine()
			coin.start_payment()
			coin.coin_machine_payment(price)
			coin.stop_payment()

	def call_printer(self):
		printer = Printer
		printer.print_ticket(self)

	def cancel_payment(self):
		overview = PurchaseOverview
		overview.cancel_payment

#region UI Set-up below -- you don't need to change anything

	def widgets(self):
		self.master.title("Ticket machine")
		menubar = tk.Menu(self.master)
		self.master.config(menu=menubar)

		fileMenu = tk.Menu(menubar)
		fileMenu.add_command(label="Exit", command=self.on_exit)
		menubar.add_cascade(label="File", menu=fileMenu)

		# retrieve the list of stations
		data2 = Tariefeenheden.get_stations()

		stations_frame = tk.Frame(self.master, highlightbackground="#cccccc", highlightthickness=1)
		stations_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)
		# From station
		tk.Label(stations_frame, text = "From station:").grid(row=0, padx=5, sticky=tk.W)
		self.from_station = tk.StringVar(value=data2[0])
		tk.OptionMenu(stations_frame, self.from_station, *data2).grid(row=1, column=0, padx=5, sticky=tk.W)

		# To station
		tk.Label(stations_frame, text = "To station:").grid(row=0, column=5, sticky=tk.W)
		self.to_station = tk.StringVar(value=data2[0])
		tk.OptionMenu(stations_frame, self.to_station, *data2).grid(row=1, column=5, sticky=tk.W)

		ticket_options_frame = tk.Frame(self.master, highlightbackground="#cccccc", highlightthickness=1)
		ticket_options_frame.pack(fill=tk.BOTH, expand=1, padx=10)

		# Class
		tk.Label(ticket_options_frame, text = "Travel class:").grid(row=1, column= 0, sticky=tk.W)
		self.travel_class = tk.IntVar(value=UIClass.SecondClass.value)
		tk.Radiobutton(ticket_options_frame, text="First class", variable=self.travel_class, value=UIClass.FirstClass.value).grid(row=5, column=0, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, text="Second class", variable=self.travel_class, value=UIClass.SecondClass.value).grid(row=6, column=0, sticky=tk.W)

		# Way
		tk.Label(ticket_options_frame, text = "Way:").grid(row=7, column= 0, sticky=tk.W)
		self.way = tk.IntVar(value=UIWay.OneWay.value)
		tk.Radiobutton(ticket_options_frame, text="One-way", variable=self.way, value=UIWay.OneWay.value).grid(row=8, column=0, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, text="Return", variable=self.way, value=UIWay.Return.value).grid(row=9, column=0, sticky=tk.W)

		# Discount
		tk.Label(ticket_options_frame, text = "Discount:").grid(row=10, column= 0, sticky=tk.W)
		self.discount = tk.IntVar(value=UIDiscount.NoDiscount.value)
		tk.Radiobutton(ticket_options_frame, text="No discount", variable=self.discount, value=UIDiscount.NoDiscount.value).grid(row=11, column=0,  sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, text="20% discount", variable=self.discount, value=UIDiscount.TwentyDiscount.value).grid(row=12, column=0, sticky=tk.W)
		tk.Radiobutton(ticket_options_frame, text="40% discount", variable=self.discount, value=UIDiscount.FortyDiscount.value).grid(row=13, column=0, sticky=tk.W)

		payment_frame = tk.Frame(self.master, highlightbackground="#cccccc", highlightthickness=1)
		payment_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

		# Payment
		tk.Label(payment_frame, text = "Payment:").grid(row=14, sticky=tk.W)
		self.payment = tk.IntVar(value=UIPayment.Cash.value)
		tk.Radiobutton(payment_frame, text="Cash", variable=self.payment, value=UIPayment.Cash.value).grid(row=15, column=0,  sticky=tk.W)
		tk.Radiobutton(payment_frame, text="Credit Card", variable=self.payment, value=UIPayment.CreditCard.value).grid(row=16, column=0,  sticky=tk.W)
		tk.Radiobutton(payment_frame, text="Debit Card", variable=self.payment, value=UIPayment.DebitCard.value).grid(row=17, column=0, sticky=tk.W)

		amount_tickets_frame = tk.Frame(self.master, highlightbackground="#cccccc", highlightthickness=1)
		amount_tickets_frame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

		# Choose Amount of Tickets
		tk.Label(amount_tickets_frame, text = "How many tickets?").grid(row=18, column= 0, columnspan=3, sticky=tk.W)
		self.amount_tickets = tk.IntVar(value=UITicketAmount.AmountTickets)
		tk.Button(amount_tickets_frame, text="-10", command=lambda: self.add_tickets(-10), width=0).grid(row=19, column= 0, sticky=tk.W, padx=5, pady=10)
		tk.Button(amount_tickets_frame, text="-5", command=lambda: self.add_tickets(-5)).grid(row=19, column= 1, sticky=tk.W, padx=5, pady=10)
		tk.Button(amount_tickets_frame, text="-1", command=lambda: self.add_tickets(-1)).grid(row=19, column= 2, sticky=tk.W, padx=5, pady=10)
		tk.Label(amount_tickets_frame, textvariable=self.amount_tickets).grid(row=19, column=3, sticky=tk.W, padx=5, pady=10)
		tk.Button(amount_tickets_frame, text="+1", command=lambda: self.add_tickets(+1)).grid(row=19, column= 4, sticky=tk.W, padx=5, pady=10)
		tk.Button(amount_tickets_frame, text="+5", command=lambda: self.add_tickets(+5)).grid(row=19, column= 5, sticky=tk.W, padx=5, pady=10)
		tk.Button(amount_tickets_frame, text="+10", command=lambda: self.add_tickets(+10)).grid(row=19, column= 6, sticky=tk.W, padx=5, pady=10)
		
		# Pay button
		tk.Button(self.master, text="Pay", command=self.on_click_pay).pack(side=tk.RIGHT, ipadx=10, padx=10, pady=10)

		self.pack(fill=tk.BOTH, expand=1)
		
	def add_tickets(self, amount_added):
		add = self.amount_tickets.get() + amount_added
		if add > 1:
			self.amount_tickets.set(add)
		else:
			self.amount_tickets.set(1)
	
	def on_click_pay(self):
		tariefeenheden = self.get_tariefeenheden(self.get_ui_info())
		discount = self.get_discount(self.get_ui_info())
		train_class = self.get_class(self.get_ui_info())
		amount_tickets = self.amount_tickets.get()
		way = self.get_ticket_type(self.get_ui_info())

		price = self.calc_price(way, tariefeenheden, discount, train_class, amount_tickets)
		price = self.credit_card_price(self.get_ui_info(), price)
		if self.show_overview(self.get_ui_info(), discount, price, amount_tickets, train_class):
			self.do_payment(self.get_ui_info(), price)
			self.call_printer()
		else:
			self.cancel_payment()

	def get_ui_info(self) -> UIInfo:
		return UIInfo(
			from_station=self.from_station.get(),
			to_station=self.to_station.get(),
			travel_class=self.travel_class.get(),
			way=self.way.get(),
			discount=self.discount.get(),
			payment=self.payment.get(),
			amount_tickets=self.amount_tickets.get()
			)

	def on_exit(self):
		self.quit()

#endregion


def main():
	root = tk.Tk()
	UI(root)
	root.mainloop()


if __name__ == '__main__':
	main()
