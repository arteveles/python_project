# Целые числа
int
1, 2, 3, -1, -2, -3

# плавающие
float
1.1, 2.4, 3.14

# строки

str
"Hello World"
x = 'Alex'
print(f"\nСтрока в одиночных кавычках x = 'Alex': \n{x}")

y = "Alex"
print(f"\nСтрока в двойных кавычках y = \"Alex\": \n{y}")

z = "Some 'long' text"
print(f"\nДлинная строка в двойных кавычках z = \"Some 'long' text\": \n{z}")


x = 'Some \'long\' and \'awesome\' text'
print(f"\nДлинная строка в одиночных кавычках x = 'Some \'long\' and \'awesome\' text': \n{x}")


y = 'C:\\Users\\dev\\python_project'
print(f"\nУказываем путь к файлу через двойной обратный слэш:  \n{y}")

y = r'C:\Users\dev\python_project'
print(f"\nУказываем путь к файлу используя r: \n{y}")

z = 'some long text \nand new string \nand new string \nand new string'
print(f"\nПеренос строк используя n: \n{z}")

print("\nРабота со строками")
# text = str('hello world')
# print(text)
# print(text[0])
#
# res = eval('text[-1]+text[1]')
# print(f"Конкатенация = сложение строк. На данном примере складываем эементы под определенными индексами text[-1]+text[1]': \n{res}")
#
# res = eval('text[6:]+text[1]')
# print(f"Получение всех элементов после 6 элемента text[6:]+text[1]: \n{res}")
#
# res = eval('text[::1]')
# print(f"Вывод элементов с шагом 1, используя ::1  \n{res}")
#
# res = eval('text[::2]')
# print(f"Вывод элементов с шагом 2, используя ::2  \n{res}")
#
#
# print(f"Функции для работы со строками, для начала объявим переменную 'some long and awesome TEXT'")
# x_text = 'some long and awesome TEXT. asd'
#
#
# podschet_simvolov_strok = eval('len(x_text)')
# print(f"Подсчет символов строк len(x_text): \n{podschet_simvolov_strok}")
#
#
# div_str = eval('x_text[len(x_text)-1]')
# print(f"Вычитание 1 элемента 'x_text[len(x_text)-1': \n{div_str}")
#
#
# div_str_s4_elem = eval('x_text[len(x_text)-4:len(x_text)]')
# print(f"Вычитание 4 элемента x_text[len(x_text)-4:len(x_text)]: \n{div_str_s4_elem}")
#
#
# print(f"Введите букву, для подсчета общего кол-ва:")
# podschet_bukv = eval('x_text.count(input())')
# print(f"Результат подсчета букв x_text.count(): \n{podschet_bukv}")
#
#
# print(f"Введите букву:")
# nomer_indeksa = eval('x_text.find(input())')
# print(f"Найти под каким индексом находится символ x_text.find('СИМВОЛ'): \n{nomer_indeksa}")
#
#
# print("Поиск с 3го по 7й символ:")
# print(x_text.find('o', 3, 7))
#
#
# print(f"Смена регистра первого символа\n", x_text.capitalize())
#
# print(f"Перевод всех символов в верхний регистр\n", x_text.upper())
#
# print(f"Перевод всех символов в нижний регистр\n", x_text.lower())


data_examp = '3; 5; 6; 7'
separated_data_examp = data_examp.split(';')
print(separated_data_examp)
print(separated_data_examp[3])

# списки - хранят последовательность объектов. Сожержит элементы различных типов данных
list
[1, 2, 3.14, 'Hello']


# словари - список пар, ключ:значение. Пример: ключ это ник-нейм а значение - id
dict
{'Alex': '12', 'Anna': '18'}


# кортежи - неизменяемый список значений. Обладают всеми свойствами list
tuple
(1, 2, 3.14, 'Hello')

# множество - последовательность уникальных объектов, дубликаты исключены
set
{'a', 'b', 'c'}

# булева логика: истина или ложь
bool
True
False

