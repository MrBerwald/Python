"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове."""

my_str=input("Введите строку: ")
word = []
n = 1
for el in range(my_str.count(' ') + 1):
    word = my_str.split()
    if len(str(word)) <= 10:
        print(f" {n} {word [el]}")
        n += 1
    else:
        print(f" {n} {word [el] [0:10]}")
        n += 1