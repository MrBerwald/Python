# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


my_list = [element for element in range(99, 1001) if element % 2 == 0]

def my_func(el1, el2):
    return el1 * el2

print(my_list)
print(reduce(my_func, my_list))