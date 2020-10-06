import numpy as np


class Matrix:

    def __init__(self, A, b):
        if A.shape[0] != b.shape[0]:
            raise Exception('matrix dimension error')
        self.A = A
        self.b = b
        self.B = None
        self.q = None
        self.xk = np.zeros(b.shape[0])

    def find_matrix(self):
        self.q = self.b / self.A.diagonal()
        self.B = self.A / (-1 * self.A.diagonal()[:, None])
        np.fill_diagonal(self.B, np.zeros(self.q.shape[0]))

    def simple_iteration_method(self):
        c = self.A.dot(self.xk) != self.b
        while c.all():
            self.xk = self.B.dot(self.xk) + self.q
            c = self.A.dot(self.xk) != self.b
        return self.xk

    def get_xk(self):
        self.find_matrix()
        return self.simple_iteration_method()


if __name__ == "__main__":
    # Матрица A(по условию квадратная на множестве рациональных чисел)
    A = np.array([[2.0, 0.5, 0.1], [1.0, 5.0, 0.7], [0.6, 1.01, 8.0]])
    # Вектор b(по условию на множестве рациональных чисел)
    b = np.array([3.0, 3.0, 1.5])
    matrix = Matrix(A, b)
    print(f'x* = {matrix.get_xk()}')

