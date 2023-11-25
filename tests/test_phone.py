import pytest

from src.item import Item
from src.phone import Phone


@pytest.mark.parametrize(
    "name_phone, price, quantity, number_of_sim", [("samsung", 30000, 10, 2), ("nokia", 10000, 5, 1)]
)
def test_class_phone(name_phone, price, quantity, number_of_sim):
    item1 = Item("iphone se", 5000, 1)
    phone1 = Phone(name_phone, price, quantity, number_of_sim)
    assert phone1.number_of_sim == number_of_sim
    assert phone1 + item1 == 1 + quantity
    assert phone1.calculate_total_price() == quantity * price
    assert repr(phone1) == f"Phone{name_phone, price, quantity, number_of_sim}"
    assert str(phone1) == name_phone
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
        phone1.number_of_sim = 1.5
