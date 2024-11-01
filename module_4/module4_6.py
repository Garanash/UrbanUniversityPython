"""
Создайте новый класс Buiding с атрибутом total
Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса Building total
В цикле создайте 40 объектов класса Building и выведите их на экран командой print
Полученный код напишите в ответ к домашнему заданию
"""
class Building:
    _total = 0
    def __init__(self):
        self.__class__._total += 1

    @classmethod
    def get_total(cls):
        # Метод для получения текущего количества объектов класса
        return cls._total

for i in range(40):
    new = Building()
    print(Building.get_total())
