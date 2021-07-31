# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        data = []

        for el in day_month_year.split():
            if el != '-': data.append(el)

        return int(data[0]), int(data[1]), int(data[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Всё в порядке'
                else:
                    return f'incorrect year'
            else:
                return f'incorrect month'
        else:
            return f'incorrect day'

    def __str__(self):
        return f'Now its {Data.extract(self.day_month_year)}'


d = Data('31 - 07 - 2021')
print(d)
print(Data.valid(1, 12, 2020))
print(d.valid(1, 12, 2020))
print(Data.extract('11 - 11 - 2011'))
