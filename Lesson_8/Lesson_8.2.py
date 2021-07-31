# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByZero:
    def __init__(self, devid, denomin):
        self.devid = devid
        self.denomin = denomin


    @staticmethod
    def d_by_null(devid, denomin):
        try:
            return (devid / denomin)
        except:
            return f'Division by zero is not allowed!'

d = DivisionByZero(10, 100)
print(d.d_by_null(10, 0))
print(d.d_by_null(10, 0.1))
print(d.d_by_null(2, 0))

