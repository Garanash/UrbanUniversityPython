"""
Создайте новый класс Building
Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
Полученный код напишите в ответ к домашнему заданию
"""
class Building:
    def __init__(self, type, floor):
        self.buildingType = type
        self.numberOfFloors = floor
    def __eq__(self, other):
        if self.numberOfFloors > other.numberOfFloors:
            return self
        elif self.numberOfFloors < other.numberOfFloors:
            return other
        else:
            if self.buildingType > other.buildingType:
                return self
            elif self.buildingType < other.buildingType:
                return  other
            else:
                return 'Да они одинаковые'
    def __repr__(self):
        return f'Building class:{self.buildingType} floors:{self.numberOfFloors}'

mb1 = Building('A',4)
mb2 = Building('B',5)
mb3 = Building('S',4)
mb4 = Building('A',4)
print(mb1 == mb2)
print(mb1 == mb3)
print(mb1 == mb4)
print(mb2 == mb3)