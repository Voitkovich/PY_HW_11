# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), 
# которые вы уже решали. Превратите функции в методы класса, 
# а параметры в свойства. Задания должны решаться через вызов методов экземпляра. 
# (Например: Треугольник дз1, дроби дз2)


class Triangle:

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def any_triangle(self):
        if (self.a + self.b < self.c or 
            self.a + self.c < self.b or 
            self.c + self.b < self.a):
            print("Такаго треугольника не существует")
        
        elif self.a == self.b == self.c:
             print("Это равносторонний треугольник")  

        elif (self.a == self.b or 
              self.b == self.c or 
              self.a == self.c):
              print("Это равнобедренный треугольник")   
        
        elif self.a != self.b != self.c:
             print("Это разносторонний треугольник") 

any_a = Triangle(1234, 2412, 1341)
any_b = Triangle(3, 3, 3)
any_c = Triangle(5,2341324, 8)
print(any_a.any_triangle())
print(any_b.any_triangle())
print(any_c.any_triangle())

    
