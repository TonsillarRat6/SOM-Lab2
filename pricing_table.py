class PricingTable:
    @staticmethod
    def get_price(tariefeenheden: int, discount: int, trainClass: int, amount_tickets: int) -> float:
        price = 0
        if trainClass == 1:
            price = 3.60
        else:
            price = 2.10

        if discount <= 1:
            price = round(price * (1-discount), 1)
        else:
            raise Exception("De korting is boven de 100%")

        price = price * 0.02 * tariefeenheden 
        return round(price, 2) * amount_tickets
