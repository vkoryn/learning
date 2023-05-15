# from test import helper
#
# helper.print_text()


# class Vehicle:
#     def __init__(self, max_speed=None):
#         self._max_speed = max_speed
#
#     @property
#     def max_speed(self):
#         return self._max_speed
#
#     @max_speed.setter
#     def max_speed(self, value):
#         self._max_speed = value
#
# class Car(Vehicle):
#     def __init__(self, max_speed=None):
#         super().__init__(max_speed)
#
# class Bicyle(Vehicle):
#     def __init__(self, max_speed=None):
#         super().__init__(max_speed)
#
# car = Car(250)
# bycicle = Bicyle(70)
# print(car.max_speed, bycicle.max_speed)


class Vehicle:
    def __init__(self, max_speed=None):
        self._max_speed = max_speed
#
#     @property
#     def max_speed(self):
#         return self._max_speed
#
#     @max_speed.setter
#     def max_speed(self, value):
#         self._max_speed = value
#
#     def go(self, speed):
#         if self.speed_is_ok(speed):
#              print('как-то едет')
#
#     def speed_is_ok(self, speed):
#         if speed <= self._max_speed:
#             return True
#         print('Не могу так быстро')
#         return False
#
# class Car(Vehicle):
#     def __init__(self, max_speed=None):
#         super().__init__(max_speed)
#
#     def go(self, speed):
#         if self.speed_is_ok(speed):
#              print('давим на газ')
#
# class Bicyle(Vehicle):
#     def __init__(self, max_speed=None):
#         super().__init__(max_speed)
#
#     def go(self, speed):
#         if self.speed_is_ok(speed):
#             print('крутим педали')
#
#     def jump(self):
#         print('прыг')
#
# class Samokat(Vehicle):
#     def __init__(self, max_speed=None):
#         super().__init__(max_speed)
#
#
# car = Car(250)
# bycicle = Bicyle(70)
# car.go(250)
# bycicle.go(100)
# samokat = Samokat(20)
# samokat.go(15)
# bycicle.jump()
# print(car.max_speed, bycicle.max_speed)

# #data1.txt
# {"Country": "Turkey", "avr_temp": 30}
# #data2.txt
# {"Country": "Greece", "avr_temp": 28}
# #data3.txt
# {"Country": "North Pole", "avg_temp": 5}
#
# import json
#
# class DataFile:
#     def __init__(self, filename):
#         self.filename = filename
#         self.data = json.loads(self.read_file())
#         self.country = self.data['Country']
#         self.avg_temp = self.data['avg_temp']
#
#     def read_file(self):
#         with open(self.filename, 'r') as txt_file:
#             return txt_file.read()
#
#
#     def is_hot(self):
#         return 'hot' if self.avg_temp > 25 else 'cold'
#
# data1 = DataFile('data1.txt')
# data2 = DataFile('data2.txt')
# data3 = DataFile('data3.txt')
# print(data1.filename, data1.country, data1.avg_temp, data1.is_hot())
# print(data2.filename, data2.country, data2.avg_temp, data2.is_hot())
# print(data3.filename, data3.country, data3.avg_temp, data3.is_hot())

# x = 1
# a = str(x)
# b = x.__str__()
# c = x.__repr__()
# print(type(c))
# print(type(b))
# print(type(a))
# print(type(x))

# class Bycicle(Vehicle):
#     def __init__(self, max_speed=None):
#         super().__init__(max_speed)
#
#     def __str__(self):
#         return f'bycile with max speed {self._max_speed}'
#
#     def go(self, speed):
#         if self.speed_is_ok(speed):
#             print('крутим педали')
#
#     def jump(self):
#         print('прыг')
#
# bycicle = Bycicle(20)
# print(bycicle)


# class Bycicle(Vehicle):
#     def __init__(self, max_speed=None):
#         super().__init__(max_speed)
#
#     def __int__(self):
#         return self._max_speed
#
#     def go(self, speed):
#         if self.speed_is_ok(speed):
#             print('крутим педали')
#
#     def jump(self):
#         print('прыг')
#
# bycicle = Bycicle(20)
# print(int(bycicle))

# a = 1
# b = 2
# print(a == b)
# print(a.__eq__(b))

# class Bycicle(Vehicle):
#     def __init__(self, max_speed=None):
#         super().__init__(max_speed)
#
#     def __eq__(self, obj):
#         return self._max_speed == obj._max_speed
#
#     def go(self, speed):
#         if self.speed_is_ok(speed):
#             print('крутим педали')
#
#     def jump(self):
#         print('прыг')
#
# bycicle = Bycicle(20)
# bycicle2 = Bycicle(20)
# print(bycicle == bycicle2)

class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money

ivan = Student('Ivan', 120)
oleg = Student('Oleg', 150)
sergei = Student('Sergei', 200)

def most_money(students):
    money = 0
    name = ''
    for s in students:
        if s.money > money:
            money = s.money
            name = s.name
    return name

print(most_money([ivan, oleg, sergei]))








