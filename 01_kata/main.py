import random

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

    def apply(self, shopping_cart: list[Item]):
        list_of_items = [i.code for i in shopping_cart]
        if (list_of_items.count(self.item) >= self.number_items):
            for i in shopping_cart:
                if (i.code == self.item):
                    i.price = self.price

class BuyXPayYRule:
    def __init__(self, item: str, n_buy: int, n_pay: int):
        self.item = item
        self.n_buy = n_buy
        self.n_pay = n_pay

    def apply(self, shopping_cart: list[Item]):
        list_of_items = [i.code for i in shopping_cart]
        if (self.item in list_of_items):
            free_items = self.n_buy - self.n_pay
            groups_of_items = list_of_items.count(self.item) // self.n_buy
            if (groups_of_items > 0):
                get_indexes = [index for index, el in enumerate(shopping_cart) if el.code == self.item]
                final_indexes = random.sample(get_indexes, free_items)
                for i in final_indexes:
                    shopping_cart[i].price = 0.0


class PricingRules:
    def __init__(self):
        self.__list_of_rules = []

    def append_rule(self, rule):
        self.__list_of_rules.append(rule)

    def get_rules(self):
        return self.__list_of_rules

    def delete_rules(self):
        self.__list_of_rules = []



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
