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
    pricing_rules = PricingRules().append_rule(rule)
    checkout = Checkout(pricing_rules)
    for item in [item1, item2]:
        checkout.scan(item)
    assert checkout.get_shopping_cart() == [item1.code, item2.code]
