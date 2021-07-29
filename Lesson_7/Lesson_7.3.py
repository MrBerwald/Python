

class Cell:
    def __init__(self, amount):
        self.amount = int(amount)
        self.simbol = '*'


    def __str__(self):
        return f'Result operation = {self.amount * "*"}'

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if int(Cell(self.amount - other.amount)) > 0:
            return Cell(int(self.amount - other.amount))
        else:
            return f'Operation is not possible'

    def __mul__(self, other):
        return self.amount * other.amount

    def __truediv__(self, other):
        return int(self.amount // other.amount)


    # def make_order(self, row):
    #     for el in row:
    #         if el >= 5:




cell1 = Cell(12)
cell2 = Cell(2)
print(cell1)
print(cell1 + cell2)
print(cell1 / cell2)
print(cell1 * cell2)
# print(cell1.make_order(12))


