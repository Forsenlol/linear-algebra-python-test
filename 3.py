import numpy as np
from queue import Queue
from threading import Thread


result = list()


def get_result():
    return np.array([i[1] for i in sorted(result, key=lambda k: k[0])])


class Main:
    
    def __init__(self, A, b):
        if A.shape[0] != b.shape[0]:
            raise Exception('matrix dimension error')
        self.A = A
        self.b = b
    
    def create_threads(self):
        """Инициализация очереди"""
        queue = Queue()
        for idx in range(A.shape[0]):
            name = f'Thread #{idx}'
            my_thread = MyThread(queue, self.b, name)
            my_thread.setDaemon(True)
            my_thread.start()
        for line in A:
            queue.put(line)
        queue.join()


class MyThread(Thread):
    
    def __init__(self, queue, vector, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.queue = queue
        self.name = name
        self.vector = vector
        self.line = np.zeros(())
    
    def run(self):
        """Запуск потока"""
        self.line = self.queue.get()
        result.append((self.name, self.line.dot(self.vector)))
        self.queue.task_done()


if __name__ == "__main__":
    # Матрица, которую нужно умножить
    A = np.array([[2.0, 0.5, 0.1], [1.0, 5.0, 0.7], [0.6, 1.01, 8.0]])
    # Вектор, на который нужно умножить
    b = np.array([3.0, 3.0, 1.5])
    m = Main(A, b)
    m.create_threads()
    print(get_result())
