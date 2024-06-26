"""
Задайте переменные разных типов данных:
  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
  - Выполните операции вывода кортежа immutable_var на экран.

3. Изменение значений переменных:
  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

4. Создание изменяемых структур данных:
  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
  - Измените элементы списка mutable_list.
  - Выведите на экран измененный список mutable_list.
"""

immutable_var = (1, "34", [])
try:
    immutable_var[1] = "345"
except TypeError:
    print("Кортеж не изменяемая структура данных")
finally:
    immutable_var[2].append(1)
    # а такое вполне законно) ибо мы меняем список влодженный в кортеж а не кортеж
print(immutable_var)

mutable_list = [1, "34", []]
mutable_list[0] = 5  # а тут мы можем заменять все что хотим
mutable_list[1] = 6
mutable_list[2] = 7
print(mutable_list)
