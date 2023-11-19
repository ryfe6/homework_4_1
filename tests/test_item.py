"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.mark.parametrize(
    "name, price, quantity, sell, expected_result",
    [("Телевизор", 45000, 10, 22500, 450000), ("Ноутбук", 20000, 5, 10000, 100000)],
)
def test_class_Item(name, price, quantity, sell, expected_result):
    item_assert = Item(name, price, quantity)
    assert item_assert.calculate_total_price() == expected_result
    assert item_assert.name == name
    assert item_assert.price == price
    assert item_assert.quantity == quantity
    Item.pay_rate = 0.5
    assert item_assert.apply_discount() == sell


def test_class_item_2():
    item = Item("Монитор", 15000, 3)
    Item.instantiate_from_csv("tests/items.csv")
    assert item.name == "Монитор"
    assert len(item.all) == 5
    assert Item.string_to_number("6.0") == 6
    assert Item.string_to_number("6") == 6
    item.name = "Мегамощный телефон"
    assert item.name == "Мегамощный"


def test_class_item_3():
    item = Item("Монитор", 15000, 3)
    assert repr(item) == "Item('Монитор', 15000, 3)"
    assert str(item) == "Монитор"
