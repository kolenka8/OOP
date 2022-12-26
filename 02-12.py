from multiprocessing import Process, Lock
from time import sleep
from random import randint

class Philosopher(Process):

    THINK_INTERVAL = (15, 20)
    EAT_INTERVAL = (1, 2)

    def __init__(self, name, left_lock, right_lock):
        super().__init__(name=name)
        self.left_lock = left_lock
        self.right_lock = right_lock
    
    def eating(self):
        print('Философ {0} кушает'.format(self.name))
        sleep(randint(*Philosopher.EAT_INTERVAL))
        print('Философ {0} закончил кушать и начинает думать'.format(self.name))

    def run(self):
        while True:
            if self.left_lock.acquire():
                print('Философ {0} взял левую палочку'.format(self.name))
                if self.right_lock.acquire():
                    print('Философ {0} взял палочку'.format(self.name))
                    self.eating()
                    sleep(randint(*Philosopher.THINK_INTERVAL))
                    print('Философ {0} закончил думать и хочет кушать'.format(self.name))
                    self.right_lock.release()
                    self.left_lock.release()
                else:
                    self.left_lock.release()
                    print('Философ {} не смог поесть'.format(self.name))



class Eat:
    def __init__(self, chopsticks):
        self.chopsticks = chopsticks
        for num_phil in range(10):
            Philosopher(str(num_phil), self.chopsticks[num_phil - 1], self.chopsticks[num_phil]).start()

if __name__ == '__main__':
    chopsticks = []
    for _ in range(10):
        lock = Lock()
        chopsticks.append(lock)
    Eat(chopsticks)