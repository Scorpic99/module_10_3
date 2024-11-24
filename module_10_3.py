import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for transact in range(100):
            replenish = random.randint(50, 500)
            self.balance += replenish
            print(f'Пополнение: {replenish}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
        time.sleep(0.001)

    def take(self):
        for transact in range(100):
            replenish = random.randint(50, 500)
            print(f'Запрос на {replenish}')
            if replenish <= self.balance:
                self.balance -= replenish
                print(f'Снятие: {replenish}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


my_bank = Bank()
thread1 = threading.Thread(target=my_bank.deposit)
thread2 = threading.Thread(target=my_bank.take, daemon=True)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f'Итоговый баланс: {my_bank.balance}')
