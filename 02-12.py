from multiprocessing import Process, Lock
from time import sleep
from random import randint

class Philosopher(Process):

    THINK_INTERVAL = (5, 6)
    EAT_INTERVAL = (5, 6)

    def __init__(self, name, left_lock, right_lock):
        super().__init__(name=name)
        self.left_lock = left_lock
        self.right_lock = right_lock

    def eating(self):
        print('Философ {} кушает'.format(self.name))
        sleep(randint(*Philosopher.EAT_INTERVAL))
        print('Философ {} закончил кушать и начинает думать.'.format(self.name))
        self.right_lock.release()
        self.left_lock.release()
        print('Философ {} думает'.format(self.name))
        sleep(randint(*Philosopher.THINK_INTERVAL))
        print('Философ {} закончил думать и хочет кушать.'.format(self.name))

    def run(self):
        while True:
            if self.left_lock.acquire():
                if self.right_lock.acquire():
                    self.eating()
                else:
                    self.left_lock.release()


class Eat:
    def __init__(self, chopsticks):
        self.chopsticks = chopsticks
        for num_phil in range(5):
            Philosopher(str(num_phil), self.chopsticks[num_phil - 1], self.chopsticks[num_phil]).start()

if __name__ == '__main__':
    chopsticks = []
    for _ in range(5):
        lock = Lock()
        chopsticks.append(lock)
    Eat(chopsticks)