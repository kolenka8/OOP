from multiprocessing import Process, Lock
from time import sleep
from random import randint

class Philosopher(Process):

    THINK_INTERVAL = (2, 3)
    EAT_INTERVAL = (1, 1)
    WAIT_CHOPSTIK = 5

    def __init__(self, name, left_lock, right_lock):
        super().__init__(name=name)
        self.left_lock = left_lock
        self.right_lock = right_lock

    def run(self):
        while True:
            print('Философ {} думает'.format(self.name))
            sleep(randint(*Philosopher.THINK_INTERVAL))
            print('Философ {} закончил думать и хочет кушать'.format(self.name))
            self.eat()

    def eat(self):
        l_lock, r_lock = self.left_lock, self.right_lock
        
        l_un = l_lock.acquire(timeout=Philosopher.WAIT_CHOPSTIK)
        if l_un:
            print('Философ {} взял левую палочку'.format(self.name))

        r_un = r_lock.acquire(timeout=Philosopher.WAIT_CHOPSTIK)
        if r_un:
            print('Философ {} взял правую палочку'.format(self.name))

        if l_un and r_un:
            print('Философ {} кушает'.format(self.name))
            sleep(randint(*Philosopher.EAT_INTERVAL))
            print('Философ {} закончил кушать и начинает думать'.format(self.name))

        else:
            print('Философ {} не смог покушать'.format(self.name))
        
        if l_un:
            l_lock.release()

        if r_un:
            r_lock.release()

class Eat:
    def __init__(self, chopsticks):
        self.chopsticks = chopsticks
        for num_phil in range(4):
            Philosopher(str(num_phil), self.chopsticks[num_phil - 1], self.chopsticks[num_phil]).start()

if __name__ == '__main__':
    chopsticks = []
    for _ in range(4):
        lock = Lock()
        chopsticks.append(lock)
    Eat(chopsticks)