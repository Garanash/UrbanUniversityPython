from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            for x in data_set:
                file.writelines(str(x) + '\n')

    return write_everything


write = get_advanced_writer('example1.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
