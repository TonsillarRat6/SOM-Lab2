class PricingTable:

    # @staticmethod
    # def get_price(tariefeenheden: int, col: int) -> float:
    #     price = 0
    #     if col == 0:
    #         price = 2.10
    #     elif col == 1:
    #         price = 1.70
    #     elif col == 2:
    #         price = 1.30
    #     elif col == 3:
    #         price = 3.60
    #     elif col == 4:
    #         price = 2.90
    #     elif col == 5:
    #         price = 2.20
    #     else:
    #         raise Exception("Unknown column number")

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
