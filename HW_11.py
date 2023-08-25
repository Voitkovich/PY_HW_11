# Решить задания, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации 
# и методы вывода информации на печать.
# Создайте класс Матрица. 
# Добавьте методы для: 
# вывода на печать, сравнения, сложения, *умножения матриц



class Matrix:
    def __init__(self, matrix):
        """ Проверим, что все строки у матриц имеют одинаковую длинну"""

        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError("Неравная длинна строк матриц!!!")

        self.matrix = matrix

    def __str__(self):
        """Метод для вывода на печать"""

        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):
        """Метод для сравнения матриц"""

        return self.matrix == other.matrix

    def __add__(self, other):
        """Метод для сложения матриц"""

        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Размеры матриц не совпадают!!!")

        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)

    def __mul__(self, other):
        """Метод для умножения матриц"""

        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Длинна столбцов и строк у матриц не совпадает!!!")

        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)



m_1 = [[1, 7, 4],
          [5, 6,  8],
          [23, 11, -2],
          [10, 5, 0]]

m_2 = [[3, 2, 4],
          [5, 7,  8],
          [5, 6,  8],
          [-2, 2, 10]]

m_3 = [[5, 7, 4, 5],
          [-12, 6, 8, 0],
          [5, 0, 32, 11]]

m_4 = [[22, 2, 4, -5, 8],
          [5, 15, 8, 3, 0],
          [5, 9, 7, 1, 0]]

matr_one = Matrix(m_1)
matr_two = Matrix(m_2)
matr_three = Matrix(m_3)
matr_four = Matrix(m_4)

print ("Cложение матриц:")
print(matr_one + matr_two)

print ("Умножение матриц:")
print(matr_one * matr_three)
print(matr_one * matr_four)

print ("Cравнение матриц:")
print(matr_one == matr_one)
print(matr_one == matr_two)