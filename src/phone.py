from src.item import Item


class Phone(Item):
    """Класс дополняет сведения о товаре телефон"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count_sim: int) -> None:
        """Осуществляем проверку, что number_of_sim проходит по всем параметрам."""
        number_of_sim = count_sim
        if number_of_sim <= 0 or number_of_sim != int(number_of_sim):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = number_of_sim

    def __add__(self, other: int) -> int:
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты Item и дочерние от них")
        return self.quantity + other.quantity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self) -> str:
        return self.name
