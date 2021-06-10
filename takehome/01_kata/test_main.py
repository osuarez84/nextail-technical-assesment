from main import *
import pytest

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

def test_rule_buy_more_than_n_items():
    rule = BuyMoreThanNItemsRule("TSHIRT", 2, 19.00)
    assert (rule.item_code, rule.number_of_items, rule.price) == ("TSHIRT", 2, 19.00)

def test_rule_buy_x_pay_y():
    rule = BuyXPayYRule("VOUCHER", 3, 1)
    assert (rule.item_code, rule.n_buy, rule.n_pay) == ("VOUCHER", 3, 1)

def test_checkout_with_rule_buy_x_pay_y():
    code = "VOUCHER"
    name = "Gift Card"
    price = 5.00

    item1 = Item(code, name, price)
    item2 = Item(code, name, price)
    rule = BuyXPayYRule("VOUCHER", 2, 1)
    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule)
    checkout = Checkout(pricing_rules)
    for item in [item1, item2]:
        checkout.scan(item)
    checkout.checkout()
    result = checkout.total_cost()
    assert result == 5.00

def test_checkout_with_rule_buy_x_pay_y_2():
    code = "VOUCHER"
    name = "Gift Card"
    price = 5.00

    item1 = Item(code, name, price)
    item2 = Item(code, name, price)
    item3 = Item(code, name, price)
    item4 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    rule = BuyXPayYRule("VOUCHER", 2, 1)
    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule)
    checkout = Checkout(pricing_rules)
    for item in [item1, item2, item3, item4]:
        checkout.scan(item)
    checkout.checkout()
    result = checkout.total_cost()
    assert result == 30.00

def test_checkout_with_two_different_rules():
    item1 = Item("VOUCHER", "Gift Card", 5.00)
    item2 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    item3 = Item("PANTS", "Summer Pants", 7.5)
    rule1 = BuyXPayYRule("VOUCHER", 2, 1)
    rule2 = BuyMoreThanNItemsRule("TSHIRT", 3, 19.00)
    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule1)
    pricing_rules.append_rule(rule2)
    checkout = Checkout(pricing_rules)
    for item in [item1, item2, item3]:
        checkout.scan(item)
    checkout.checkout()
    result = checkout.total_cost()
    assert result == 32.5

def test_checkout_with_two_different_rules_2():
    item1 = Item("VOUCHER", "Gift Card", 5.00)
    item2 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    item3 = Item("VOUCHER", "Gift Card", 5.00)
    rule1 = BuyXPayYRule("VOUCHER", 2, 1)
    rule2 = BuyMoreThanNItemsRule("TSHIRT", 3, 19.00)
    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule1)
    pricing_rules.append_rule(rule2)
    checkout = Checkout(pricing_rules)
    for item in [item1, item2, item3]:
        checkout.scan(item)
    checkout.checkout()
    result = checkout.total_cost()
    assert result == 25.0

def test_checkout_with_two_different_rules_3():
    item1 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    item2 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    item3 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    item4 = Item("VOUCHER", "Gift Card", 5.00)
    item5 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    rule1 = BuyXPayYRule("VOUCHER", 2, 1)
    rule2 = BuyMoreThanNItemsRule("TSHIRT", 3, 19.00)
    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule1)
    pricing_rules.append_rule(rule2)
    checkout = Checkout(pricing_rules)
    for item in [item1, item2, item3, item4, item5]:
        checkout.scan(item)
    checkout.checkout()
    result = checkout.total_cost()
    assert result == 81

def test_checkout_with_two_different_rules_4():
    item1 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    item2 = Item("VOUCHER", "Gift Card", 5.00)
    item3 = Item("VOUCHER", "Gift Card", 5.00)
    item4 = Item("VOUCHER", "Gift Card", 5.00)
    item5 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    item6 = Item("TSHIRT", "Summer T-Shirt", 20.00)
    item7 = Item("PANTS", "Summer Pants", 7.5)
    rule1 = BuyXPayYRule("VOUCHER", 2, 1)
    rule2 = BuyMoreThanNItemsRule("TSHIRT", 3, 19.00)
    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule1)
    pricing_rules.append_rule(rule2)
    checkout = Checkout(pricing_rules)
    for item in [item1, item2, item3, item4, item5, item6, item7]:
        checkout.scan(item)
    checkout.checkout()
    result = checkout.total_cost()
    assert result == 74.5

def test_rules_deletion_from_pricing_rules_object():
    rule1 = BuyXPayYRule("VOUCHER", 2, 1)
    rule2 = BuyMoreThanNItemsRule("TSHIRT", 3, 19.00)
    pricing_rules = PricingRules()
    pricing_rules.append_rule(rule1)
    pricing_rules.append_rule(rule2)
    pricing_rules.delete_rules()
    assert pricing_rules.get_rules() == []

def test_class_item_validation_price():
    with pytest.raises(ValueError):
        Item("TSHIRT", "Summer T-Shirt", -20.00)

def test_class_item_validation_price_2():
    item = Item("   TSHIRT ", "    Summer T-Shirt ", 99.9)
    assert (item.code, item.name) == ("TSHIRT", "Summer T-Shirt")

def test_class_item_valudation_price_3():
    with pytest.raises(TypeError):
        Item("TSHIRT", "Summer T-Shirt", "None")

def test_class_BuyMoreThanNItemsRule_1():
    rule = BuyMoreThanNItemsRule("  TSHIRT", 7, 20)
    assert rule.item_code == "TSHIRT"


def test_class_BuyMoreThanNItemsRule_2():
    with pytest.raises(ValueError):
        BuyMoreThanNItemsRule("  TSHIRT", -7, 20)

def test_class_BuyMoreThanNItemsRule_3():
    with pytest.raises(ValueError):
        BuyMoreThanNItemsRule("  TSHIRT", 7, -20)

def test_class_BuyXPayYRule_1():
    rule = BuyXPayYRule("PANTS   ", 2, 1)
    assert rule.item_code == "PANTS"

def test_class_BuyXPayYRule_2():
    with pytest.raises(NbuyLessThanNpayError):
        BuyXPayYRule("PANTS   ", 1, 5)

def test_class_BuyXPayYRule_3():
    with pytest.raises(ValueError):
        BuyXPayYRule("PANTS   ", -3, 2)

def test_class_BuyXPayYRule_4():
    with pytest.raises(ValueError):
        BuyXPayYRule("PANTS   ", 3, -2)
