

class Item:
    def __init__(self, code: str, name: str, price: float):
        self.code = code
        self.name = name
        self.price = price

class BuyMoreThanNItemsRule:
    def __init__(self, item: str, number_items: int, price: float):
        self.item = item
        self.number_items = number_items
        self.price = price


class PricingRules:
    def __init__(self):
        self.__list_of_rules = []

    def append_rule(self, rule):
        self.__list_of_rules.append(rule)


class Checkout:
    def __init__(self, rules: PricingRules):
        self.__rules = rules
        self.__shopping_cart = []

    def scan(self, item):
        self.__shopping_cart.append(item)

    def get_shopping_cart(self):
        return [i.code for i in self.__shopping_cart]
