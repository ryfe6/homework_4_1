from src.item import Item


class MixinLang:
    """Класс служит дополнением для класса Keyboard.
       Позволяет изменять раскладку клавиатуры."""
    def __init__(self) -> None:
        self._language = "EN"

    def change_lang(self, _language: str) -> str:
        """Метод изменяет раскладку клавиатуры"""
        if _language == "EN":
            self._language = "RU"
            return self._language
        else:
            self._language = "EN"
        return self._language

    def __str__(self):
        return self._language


class Keyboard(Item, MixinLang):
    """Класс для работы с товаром клавиатура."""
    def __init__(self, name: str, price: int, quantity: int, language: str = "EN") -> None:
        super().__init__(name, price, quantity)
        self._language = language

    def change_lang(self) -> None:
        """Метод для изменения раскладки клавиатуры."""
        self._language = super().change_lang(self._language)

    @property
    def language(self) -> str:
        return self._language
