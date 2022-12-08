# Это типичный класс. Для него ВАЖНО понятие "объект"
class MyTriangles:

    # Это называется конструктор класса
    def __init__(self, tax = 0.2):
        # Это называется поле класса (относящееся к экземпляру класса)
        self.tax = tax

    # Это называется метод класса
    def hypot(self, cathet1, cathet2):
        result = cathet1 * cathet1 + cathet2 * cathet2
        result = result ** 0.5
        return result * (1 - self.tax)

    def cathet(self, hypotenuse, another_cathet):
        return (hypotenuse ** 2 - another_cathet ** 2) ** 0.5 * (1 - self.tax)

if __name__ == "__main__":

    # Создаем экземпляры класса (=объекты)
    triangles0 = MyTriangles(0.0) # фактически, это вызов конструктора класса
    # triangles0.tax = 0
    triangles10 = MyTriangles(0.1)  # фактически, это вызов конструетора класса
    # triangles10.tax = 0.1
    triangles20 = MyTriangles()  # фактически, это вызов конструетора класса

    print(triangles0.hypot(3,4), triangles10.hypot(3,4), triangles20.hypot(3,4))

