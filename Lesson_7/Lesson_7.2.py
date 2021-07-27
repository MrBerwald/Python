# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды
# использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике работу декоратора @property.


class Tx:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square_coat(self):
        return self.width / 6.5 * 0.5

    def square_suit(self):
        return self.height * 2 + 0.3

    @property
    def full_square(self):
        return str(f'Общаяя площадь - ({self.width / 6.5 * 0.5} + {self.height * 2 + 0.3})')


class Coat(Tx):
    def __init__(self, width, height):
        super().__init__(width, height)

    def __str__(self):
        return f'Площадь на пальто {self.square_coat()}'


class Suit(Tx):
    def __init__(self, width, height):
        super().__init__(width, height)

    def __str__(self):
        return f'Площадь на костюм - {self.square_suit()}'


coat = Coat(4, 12)
suit = Suit(14, 20)
print(coat)
print(suit)
print(coat.full_square)
print(suit.full_square)
print(suit.square_suit())
print(coat.square_coat())
