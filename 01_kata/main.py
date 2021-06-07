

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

    def apply(self, shopping_cart):
        list_of_items = [i.code for i in shopping_cart]
        if (list_of_items.count(self.item) >= self.number_items):
            for i in shopping_cart:
                if (i.code == self.item):
                    i.price = self.price



class PricingRules:
    def __init__(self):
        self.__list_of_rules = []

    def append_rule(self, rule):
        self.__list_of_rules.append(rule)

    def get_rules(self):
        return self.__list_of_rules

    ## TODO: add method to delete all rules


class Checkout:
    def __init__(self, rules: PricingRules):
        self.__rules = rules
        self.__shopping_cart = []

    def scan(self, item: Item):
        self.__shopping_cart.append(item)

    def get_shopping_cart(self):
        return [i.code for i in self.__shopping_cart]

    def checkout(self):
        for rule in self.__rules.get_rules():
            rule.apply(self.__shopping_cart)

    def total_cost(self):
        total = 0
        for i in self.__shopping_cart:
            total += i.price
        return total
