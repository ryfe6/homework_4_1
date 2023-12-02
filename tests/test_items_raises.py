import pytest

from src.item import InstantiateCSVError, Item


def test_class_items_isinstance_from_csv_1():
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("")


def test_class_items_isinstance_from_csv_2():
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("src/items_2.csv")
