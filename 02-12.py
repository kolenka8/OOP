from multiprocessing import Process, Lock
from time import sleep
from random import randint

class Philosopher(Process):

    THINK_INTERVAL = (5, 6)
    EAT_INTERVAL = (5, 6)

    def __init__(self, name, l_lock, r_lock):
        super().__init__(name=name)
        self.l_lock = l_lock
        self.r_lock = r_lock

    def eating(self):
        print('Philosopher {0} is eating'.format(self.name))
        sleep(randint(*Philosopher.EAT_INTERVAL))
        print('Philosopher {0} end eating and start thinking.'.format(self.name))
        self.r_lock.release()
        self.l_lock.release()
        print('Philosopher {0} is thinking'.format(self.name))
        sleep(randint(*Philosopher.THINK_INTERVAL))
        print('Philosopher {0} end thinking and want`s eating.'.format(self.name))

    def run(self):
        while True:
            if self.l_lock.acquire():
                if self.r_lock.acquire():
                    self.eating()
                else:
                    self.l_lock.release()


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