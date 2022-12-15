from multiprocessing import Process, Queue, Lock, Event
from time import sleep
from random import randint, choice

class Client:
    def __init__(self, name, serv):
        self.name = name
        self.serv = serv

class Barber:
    TIME_WAIT = 20

    def __init__(self, services):
        self.services = services
        self.client_came = Event()
    
    def sleep(self):
        print('~~~Барбер спит')
        result = self.client_came.wait(timeout=Barber.TIME_WAIT)
        return result
    
    def call(self):
        self.client_came.set()
    
    def work(self, client: Client):
        print('<- Барбер выполняет услугу {}, которую выбрал {}'.format(client.serv, client.name))
        sleep(randint(1,2))
    
    def greet(self, client: Client):
        print('! Барбер понял выбор клиента и приступает к действию {}'.format(client.name))
        self.client_came.clear()
        self.work(client)
        print('# Клиент {} доволен услугой и уходит по своим делам'.format(client.name))

class BarberShop:
    def __init__(self, services, q_size: int, lock: Lock):
        self.services = services
        self.q_size = q_size
        self.lock = lock
        self.__worker = Barber(services)
        self.__process = Process(target=self.work)
        self.__queue = Queue(maxsize=q_size)

    def open(self):
        print('Барбершоп открывается с {} местами в очереди'.format(self.q_size))
        self.__process.start()

    def close(self):
        print('Клиентов больше не приходило, Барбершоп закрыт')

    def work(self):
        while True:
            self.lock.acquire()
            if self.__queue.empty():
                self.lock.release()
                work_result = self.__worker.sleep()
                if not work_result:
                    self.close()
                    break
            else:
                self.lock.release()
                client = self.__queue.get()
                self.__worker.greet(client)

    def enter(self, client: Client):
        with lock:
            print('+ Клиент {} зашел в Барбершоп и ищет свободное место'.format(client.name))
            if self.__queue.full():
                print('- Зал ожидания заполнен, клиент {} уходит'. format(client.name))
            else:
                values = client.name, client.serv
                print('* Клиент {} выбрал услугу {}'.format(*values))
                self.__queue.put(client)
                self.__worker.call()

SIZE_QUEUE = 6
CLIENT_ENTER_INTERVAL = (3, 5)

SERVICES = [
    '(Стрижка)',
    '(Борода)',
    '(Стрижка + Борода)',
    '(Чистка лица)']

if __name__ == '__main__':
    lock = Lock()
    names = [str(i) for i in range(6)]
    clients = [Client(name, choice(SERVICES)) for name in names]
    barber_shop = BarberShop(SERVICES, SIZE_QUEUE, lock)
    barber_shop.open()
    for client in clients:
        sleep(randint(*CLIENT_ENTER_INTERVAL))
        barber_shop.enter(client)
