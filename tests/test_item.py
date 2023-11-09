"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


# @pytest.mark.parametrize('name', "price", "quantity" "expected_result", [("Телевизор", 45000, 10, 450000),
#                                                                          ("Ноутбук", 20000, 5, 100000)])
# def test_class_Item(name, price, quantity, expected_result):
#     item_1 = Item(name, price, quantity)
#     # assert print(item_assert.calculate_total_price()) == expected_result
#     i = item_1.price
#     assert i == price

@pytest.mark.parametrize("name, price, quantity, sell, expected_result", [("Телевизор", 45000, 10, 22500, 450000),
                                                                          ("Ноутбук", 20000, 5, 10000, 100000)])
def test_class_Item(name, price, quantity, sell, expected_result):
    item_assert = Item(name, price, quantity)
    assert item_assert.calculate_total_price() == expected_result
    assert item_assert.name == name
    assert item_assert.price == price
    assert item_assert.quantity == quantity
    Item.pay_rate = 0.5
    assert item_assert.apply_discount() == sell
