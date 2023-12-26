# class Bank:
#     def __init__(self):
#         self.investment: Investment = None
#
#     def profit(self):
#         return self.investment.profit()
#
# class Investment:
#     def __init__(self, money, term, percent):
#         self.amount = money
#         self.term = term
#         self.percent = percent
#
#     def profit(self):
#         print('Я считаю профит')
#         profit = None
#         return profit
#
# bank = Bank()
# my_inv = Investment(100, 12, 10)
# bank.investment = my_inv
# print(bank.profit())

# from utils import helper as h

# from time import sleep
# while True:
#     try:
#         print('ww')
#         sleep(2)
#     except KeyboardInterrupt:
#         print('Good bye')


# def my_generator():
#     my_list = [1, 2, 3, 4, 5]
#     for l in my_list:
#         yield l
#
# for x in my_generator():
#     print(x)
#
# print(list(my_generator()))

def calc(a, b, operation):
    if operation == '/':
        try:
            print(a / b)
        except ZeroDivisionError:
            print('На ноль делить нельзя')
    elif operation == '*':
        print(a*b)

calc(1, 0, '/')

