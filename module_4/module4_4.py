"""
Создайте новый класс House
Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors
Полученный код напишите в ответ к домашнему заданию
"""

class House:
    def __init__(self):
        self._numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self._numberOfFloors = floors
        print(self._numberOfFloors)

myHouse = House()
myHouse.setNewNumberOfFloors(3)