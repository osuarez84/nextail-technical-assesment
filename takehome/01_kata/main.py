from typing import Union

class Item:
    """
    A class to represent an Item.
    """
    def __init__(self, code: str, name: str, price: float):
        """
        Parameters
        ----------
        code : str
            Description code of the item.
        name : str
            The name of the item.
        price : float
            The price of the item.
        """
        self.code = code
        self.name = name
        self.price = price

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value.strip()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if (value < 0):
            raise ValueError("Price can not be less than 0.")
        self._price = value



class BuyMoreThanNItemsRule:
    """
    A class to represent a rule of 'if buying more or equal than X items,
    then item s price is Y'.

    Methods
    -------
    apply(shopping_cart)
        Apply the rule over the items in the shopping cart.
    """
    def __init__(self, item: str, number_of_items: int, price: float):
        """
        Parameters
        ----------
        item_code : str
            Name of the item for which the rule applies.
        number_of_items : int
            Number of minimum items to buy for the rule to be applied.
        price : float
            New price after the rule applies.
        """
        self.item_code = item
        self.number_of_items = number_of_items
        self.price = price

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        if not isinstance(value, str):
            raise TypeError("item_code must be a string.")
        elif len(value) > 15:
            raise ValueError("item_code can not exceed 15 characters.")
        self._item_code = value

    @property
    def number_of_items(self):
        return self._number_of_items

    @number_of_items.setter
    def number_of_items(self, value):
        if not isinstance(value, int):
            raise TypeError("number_of_items must be a number.")
        elif (value < 0) or (value > 99):
            raise ValueError("number_of_items can not be less than 0 or more than 99.")
        self._number_of_items = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Price must be a number.")
        elif (value < 0) or (value > 9999):
            raise ValueError("Price can not be less than 0 or more than 9999.")
        self._price = value

    def apply(self, shopping_cart: list[Item]):
        """
        This method applies the rule over all the items in the shopping cart.

        Parameters
        ----------
        shopping_cart : list[Item]
            The shopping cart with all the items.
        """
        list_of_items = [item.code for item in shopping_cart]
        if (list_of_items.count(self.item_code) >= self.number_of_items):
            for item in shopping_cart:
                if (item.code == self.item_code):
                    item.price = self.price

class BuyXPayYRule:
    """
    A class to represent a rule of the type 'buy X pay Y'.

    Methods
    -------
    apply(shopping_cart)
        Apply the rule over the items in the shopping cart.
    """
    def __init__(self, item: str, n_buy: int, n_pay: int):
        """
        Parameters
        ----------
        item_code : str
            Name of the item for which the rule applies.
        n_buy : int
            Number of items to buy.
        n_pay : int
            Number of items to pay.
        """
        self.item_code = item
        self.n_buy = n_buy
        self.n_pay = n_pay

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        if not isinstance(value, str):
            raise TypeError("item_code must be a string.")
        elif len(value) > 15:
            raise ValueError("item_code can not exceed 15 characters.")
        self._item_code = value

    @property
    def n_buy(self):
        return self._n_buy

    @n_buy.setter
    def n_buy(self, value):
        if not isinstance(value, int):
            raise TypeError("n_buy must be a number.")
        elif (value < 0) or (value > 10):
            raise ValueError("n_buy can not be less than 0 or more than 10.")
        self._n_buy = value

    @property
    def n_pay(self):
        return self._n_pay

    @n_pay.setter
    def n_pay(self, value):
        if not isinstance(value, int):
            raise TypeError("n_pay must be a number.")
        elif (value < 0) or (value > 10):
            raise ValueError("n_pay can not be less than 0 or more than 10.")
        self._n_pay = value



    def apply(self, shopping_cart: list[Item]):
        """
        This methos apply the rule over all the items in the shopping cart.

        Parameters
        ----------
        shopping_cart : list[Item]
            The shopping cart with all the items.
        """
        list_of_items = [item.code for item in shopping_cart]
        if (self.item_code in list_of_items):
            free_items = self.n_buy - self.n_pay
            groups_of_items = list_of_items.count(self.item_code) // self.n_buy
            if (groups_of_items > 0):
                get_indexes = [index for index, el in enumerate(shopping_cart) if el.code == self.item_code]
                final_indexes = get_indexes[:free_items]
                for ix in final_indexes:
                    shopping_cart[ix].price = 0.0


class PricingRules:
    """
    A class to gather all the rules that apply in the final checkout.

    Methods
    -------
    append_rule(rule)
        Append a new rule to the list of rules.
    get_rules()
        Get the list of all the rules.
    delete_rules()
        Delete all the rules in the object.
    """
    def __init__(self):
        self.__list_of_rules = []

    def append_rule(self, rule: Union[BuyXPayYRule, BuyMoreThanNItemsRule]):
        """
        Method to append the a rule to the list of rules inside the object.

        Parameters
        ----------
        rule : BuyXPayYRule, BuyMoreThanNItemsRule
            The type of rule that is appended to the list.
        """
        self.__list_of_rules.append(rule)

    def get_rules(self) -> list:
        """
        Method to obtain all the rules in the list.
        """
        return self.__list_of_rules

    def delete_rules(self):
        """
        Method to delete all the rules in the list.
        """
        self.__list_of_rules = []



class Checkout:
    """
    A class to represent the checkout stage of the purchase.

    Methods
    -------
    scan(item)
        Scan every item that goes into the shopping cart.
    get_shopping_cart()
        Get the whole list of items in the shopping_cart.
    checkout()
        Apply all the rules to the shopping_cart.
    total_cost()
        Get the total cost of the items in the shopping_cart.
    """
    def __init__(self, rules: PricingRules):
        """
        Parameters
        ----------
        rules : PricingRules
            A list with all the rules that are applied.
        """
        self.__rules = rules
        self.__shopping_cart: list[Item] = []

    def scan(self, item: Item):
        """
        A method to add the item to the shopping cart.

        Parameters
        ----------
        item : Item
            Item that goes into the shopping cart.
        """
        self.__shopping_cart.append(item)

    def get_shopping_cart(self) -> list[str]:
        """
        A method to get the whole list of items in the shopping cart.
        """
        return [item.code for item in self.__shopping_cart]

    def checkout(self):
        """
        A method to make the checkout of the shopping cart. During the checkout
        stage all the rules are applied to the items.
        """
        for rule in self.__rules.get_rules():
            rule.apply(self.__shopping_cart)

    def total_cost(self) -> float:
        """
        A method to get the total cost of the shopping cart.
        """
        total = 0.0
        for item in self.__shopping_cart:
            total += item.price
        return total
