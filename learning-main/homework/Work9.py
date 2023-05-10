# class Cat:
#     pow_qty = 4
#     has_tail = True
#
#
# barsik = Cat()
# murzik = Cat()
# murzik_pows = murzik.pow_qty
# barsik_pows = barsik.pow_qty
# print(murzik_pows, barsik_pows)


# class Cat:
#     pow_qty = 4
#     has_tail = True
#
#     def __init__(self, color = 'gold'):
#         self.color = color
#
# serik = Cat(color = 'grey')
# goldie = Cat()
# print(serik.color, serik.pow_qty, serik.has_tail, goldie.color)


# # data1.txt
# {'Country': 'Turkey', 'avr_temp': 30}
# # data2.txt
# {'Country': 'Greece', 'avr_temp': 28}
#
# import json
#
# def read_file(filename):
#     with open(filename, 'r') as txt_file:
#         return  txt_file.read()
#
# data1 =json.loads(read_file('data1.txt'))
# data2 = json.loads(read_file('data2.txt'))
# print(data1, data2)
# #
#
# class DataFile:
#     def __init__(self, filename):
#         self.filename = filename
#         self.data = json.loads(self.read_file())
#         self.country = self.data['Country']
#         self.avr_temp = self.data['avr_temp']
#
#     def read_file(self):
#         with open (self.filename, 'r') as txt_file:
#             return txt_file.read()
#
# data1 = DataFile('data1.txt')
# print(data1.filename, data1.country)
#
# my_var = 1
# print(type(my_var))
# print(type(data1))

# class DataFile:
#     def __init__(self, filename):
#         self._filename = filename
#         self._data = json.loads(self.read_file())
#         self._country = self._data['Country']
#         self._avr_temp = self._data['avr_temp']
#         self._done = False
#
#     def read_file(self):
#         with open (self._filename, 'r') as txt_file:
#             return txt_file.read()
#
#     @staticmethod
#     def is_hot(temp):
#         return 'hot' if temp > 25 else 'cold'
#
#     @property
#     def done(self):
#         return self._done
#
#     @done.setter
#     def done(self, value):
#         self._done = value
#
#     @done.deleter
#     def done(self):
#         del self._done
#
#
#
# data1 = DataFile('data1.txt')
# data1._country = 'India'
# print(data1._filename, data1._country)
# data1.done = True
# del data1.done
# # print(data1._done)
# print(data1.is_hot(10))

# class Worker:
#     def __init__(self, name, salary):
#         self._name = name
#         self._salary = salary
#
#     @property
#     def name(self):
#         return self._name
#
# worker1 = Worker('John', 25)
# print(worker1.name)


class Students:
    def __init__(self, name, group, marks):
        self.name = name
        self.group = group
        self.marks = marks

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_groups_students(self, group):
        result = []
        for student in self.students:
            if student.group == group:
                result.append(student.name)
        return result

my_school = School()
student1 = Students('John', 12, [1, 2, 3])
student2 = Students('Jim', 13, [1, 2, 3])
student3 = Students('Tim', 12, [1, 2, 3])
my_school.add_student(student1)
my_school.add_student(student2)
my_school.add_student(student3)
print(my_school.get_groups_students(13))




