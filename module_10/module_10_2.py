import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')

        days = 0
        while self.enemies > 0:
            self.enemies -= self.power
            days += 1

            print(f'{self.name} сражается {days} день..., осталось {self.enemies} врагов')
            time.sleep(1)

        print(f'{self.name} одержал победу спустя {days} дней!')


knight1 = Knight('Ланселот', 10)
knight2 = Knight('Галахад', 20)

knight1.start()
knight2.start()

knight1.join()
knight2.join()
