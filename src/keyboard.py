from typing import Any

from src.item import Item


class MixinLang:
    """Класс служит дополнением для класса Keyboard.
    Позволяет изменять раскладку клавиатуры."""

    def __init__(self, language: str = "EN") -> None:
        self._language = language

    def change_lang(self) -> str:
        """Метод изменяет раскладку клавиатуры"""
        if self.language == "EN":
            self._language = "RU"
            return self._language
        else:
            self._language = "EN"
        return self._language

    def __str__(self) -> Any:
        return self._language

    @property
    def language(self) -> Any:
        return self._language


class Keyboard(Item, MixinLang):
    """Класс для работы с товаром клавиатура."""

    def __init__(self, name: str, price: int, quantity: int) -> None:
        super().__init__(name, price, quantity)
