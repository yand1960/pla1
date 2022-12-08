# Это не совсем типичный класс. Для него бессмысленно понятие "объект"
class MyTriangles:

    # Это называется поле класса
    tax = 0.2

    # Это называется метод класса
    def hypot(cathet1, cathet2):
        result = cathet1 * cathet1 + cathet2 * cathet2
        result = result ** 0.5
        return result * (1 - MyTriangles.tax)

    def cathet(hypotenuse, another_cathet):
        return (hypotenuse ** 2 - another_cathet ** 2) ** 0.5 * (1 - MyTriangles.tax)

if __name__ == "__main__":
    MyTriangles.tax = 0.1
    print(MyTriangles.hypot(3,4), MyTriangles.cathet(5,4))
