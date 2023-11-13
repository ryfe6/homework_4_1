import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name_user: str) -> str:
        name = name_user
        if len(name) > 10:
            self.__name = name[0:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        """
        Инициализирует экземпляры класса используя список csv.
        """
        cls.all = []
        with (open(filename, newline="") as csvfile):
            reader = csv.DictReader(csvfile, delimiter=",")
            for line in reader:
                name = line['name']
                price = int(line['price'])
                quantity = int(line['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Строчное число преобразует в int.
        :return: Целое число
        """
        num = float(number)
        return int(num)
