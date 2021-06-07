from main import Item

def test_class_item():
    code = "VOUCHER"
    name = "Gift Card"
    price = 5.00
    item = Item(code, name, price)
    assert (item.code, item.name, item.price) == (code, name, price)
