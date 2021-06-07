from main import Item, BuyMoreThanNItemsRule, Checkout, PricingRules

def test_class_item():
    code = "VOUCHER"
    name = "Gift Card"
    price = 5.00
    item = Item(code, name, price)
    assert (item.code, item.name, item.price) == (code, name, price)


def test_checkout_scan_and_get_items():
    code = "VOUCHER"
    name = "Gift Card"
    price = 5.00

    item1 = Item(code, name, price)
    item2 = Item(code, name, price)

    rule = BuyMoreThanNItemsRule(code, 2, price)
    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule)

    checkout = Checkout(pricing_rules)

    for item in [item1, item2]:
        checkout.scan(item)
    assert checkout.get_shopping_cart() == [item1.code, item2.code]


def test_pricing_rules():
    code = "VOUCHER"

    rule = BuyMoreThanNItemsRule(code, 2, 3.00)
    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule)
    assert pricing_rules.get_rules()[0].price == 3.00


def test_checkout_method_from_checkout_object():
    code = "VOUCHER"
    name = "Gift Card"
    price = 5.00

    item1 = Item(code, name, price)
    item2 = Item(code, name, price)

    rule = BuyMoreThanNItemsRule(code, 2, 3.00)

    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule)

    checkout = Checkout(pricing_rules)

    for item in [item1, item2]:
        checkout.scan(item)
    checkout.checkout()
    result = checkout.total_cost()
    assert result == 6.00

def test_checkout_method_from_checkout_object_3_items():
    code = "VOUCHER"
    name = "Gift Card"
    price = 5.00

    item1 = Item(code, name, price)
    item2 = Item(code, name, price)
    item3 = Item("TSHIRT", "Summer T-Shirt", 20.00)

    rule = BuyMoreThanNItemsRule(code, 2, 3.00)

    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule)

    checkout = Checkout(pricing_rules)

    for item in [item1, item2, item3]:
        checkout.scan(item)
    checkout.checkout()
    result = checkout.total_cost()
    assert result == 26.00

def test_checkout_method_from_checkout_object_3_items_2_same_rules():
    code = "VOUCHER"
    name = "Gift Card"
    price = 5.00

    item1 = Item(code, name, price)
    item2 = Item(code, name, price)
    item3 = Item("TSHIRT", "Summer T-Shirt", 20.00)

    rule1 = BuyMoreThanNItemsRule(code, 2, 3.00)
    rule2 = BuyMoreThanNItemsRule("TSHIRT", 1, 19.00)

    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule1)
    pricing_rules.append_rule(rule2)

    checkout = Checkout(pricing_rules)

    for item in [item1, item2, item3]:
        checkout.scan(item)
    checkout.checkout()
    result = checkout.total_cost()
    assert result == 25.00
