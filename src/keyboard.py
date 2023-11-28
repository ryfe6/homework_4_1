from src.item import Item


class MixinLang:
    """Класс служит дополнением для класса Keyboard.
    Позволяет изменять раскладку клавиатуры."""

    def __init__(self) -> None:
        self._language = "EN"

    def change_lang(self) -> str:
        """Метод изменяет раскладку клавиатуры"""
        if self._language == "EN":
            self._language = "RU"
            return self._language
        else:
            self._language = "EN"
        return self._language

    def __str__(self) -> str:
        return self._language


class Keyboard(Item, MixinLang):
    """Класс для работы с товаром клавиатура."""

    def __init__(self, name: str, price: int, quantity: int, language: str = "EN") -> None:
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self) -> str:
        return self._language
