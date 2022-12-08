# Наследование

from pla14_OOP2 import MyTriangles

class MyTriaglesExtended(MyTriangles):

    # Расширение предка
    def height(self, cathet1, cathet2):
        return cathet1 * cathet2 / self.hypot(cathet1, cathet2) * (1 - self.tax)

    # Переркываем метод предка (досташийся от дедушки)
    def __str__(self):
        return f"I am объект расширенного класса треугольников. Мой налог: {self.tax}"

if __name__ == "__main__":
    mte = MyTriaglesExtended(0.1)
    print(mte.hypot(3, 4), mte.height(3, 4))

    print(mte)