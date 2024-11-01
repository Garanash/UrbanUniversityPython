import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount} Баланс: {self.balance}")

            # Разблокировка замка, если баланс >= 500
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            time.sleep(0.001)

    def take(self):
        for i in range(100):
            amount = random.randint(50, 500)

            print(f"Запрос на {amount}")

            # Проверка баланса и снятие средств
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount} Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")

                # Блокировка потока
                self.lock.acquire()

        # Разблокировка потока после завершения цикла снятия
        self.lock.release()


bk = Bank()

# Создание и запуск потоков
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f"Итоговый баланс: {bk.balance}")
