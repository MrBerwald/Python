


def my_func():
    try:
        var1 = int(input("Введите число: "))
        var2 = int(input("Введите второе число: "))
        return var1 / var2
    except ZeroDivisionError:
        return print("Division by zero")
    except ValueError:
        return print("ValueError")

print(my_func())
