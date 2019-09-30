# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def go(self):
        print('Going...')

    def stop(self):
        print('Stopped...')

    def turn(self, direction):
        if direction == 'right':
            print('Car turning ' + direction)
        elif direction == 'left':
            print('Car turning ' + direction)
        else:
            print('Wrong direction')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__()
        self.car_type = 'TownCar'
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__()
        self.car_type = 'SportCar'
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

class WorkCar(Car):
    def __init__(self, speed, name):
        super().__init__()
        self.car_type = 'WorkCar'
        self.speed = speed
        self.color = 'Yellow'
        self.name = name
        self.is_police = False

class PoliceCar(Car):
    def __init__(self, speed):
        super().__init__()
        self.car_type = 'PoliceCar'
        self.speed = speed
        self.color = 'Blue and White'
        self.name = 'Ford'
        self._is_police = True

car_1 = PoliceCar(200)
car_1.turn('left')
print(car_1._is_police)