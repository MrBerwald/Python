# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def account(name, surname, birthday, city, email, tel):
    return ' '.join([name, surname, birthday, city, email, tel])

print(account(name='alex', surname='baerwald', birthday='1995', city='Berlin', email='mrberwald@gmail.com', tel='222'))

