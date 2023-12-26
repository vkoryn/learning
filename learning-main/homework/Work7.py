# def my_func(a, b):
#     global c
#     b, a = a, b
#     d = 'Mike'
#     print(a, b, c, d)
#
# a, b, c, d = 1, 2, 'c is global', 4
# my_func(11, 22)
# print(a, b, c, d)

# def outer():
#     x = 'local'
#
#     def inner():
#         nonlocal x
#         x = 'nonlocal'
#         print('inner', x)
#
#     inner()
#     print('outer', x)
# outer()

# def my_fun(x):
#     return x * 3
#
# ==
#
# my_fun = lambda x: x * 3
# l = [1, 2, 3, 4]
#
#
# def modify_list(lst, fn):
#     lst1 = []
#     for el in lst:
#         lst1.append(fn(el))
#     return lst1
#
#
# def increase(x):
#     return x + 5
#
#
# def multiply(x):
# #     return x * 5
#
# print(modify_list(l, multiply))
# print((modify_list(l, lambda x: x * 5)))

# L = [1, 2, 3, 4]
#
# # def sq(x):
# #     return x ** 2
#
# print(list(map(lambda x: x ** 2, L)))

# L = [1, 2, 3, 4]
#
# print(list(filter(lambda x: x % 2 == 0, L)))

# employs = [{'name': 'john', 'age': 38}, {'name': 'Viktar', 'age': 33}]
# print(employs)
# print(sorted(employs, key=lambda x: x['age']))
#
# a = 24
# b = 25
# print(id(a), id(b))
# print(hash(a), hash(b))

from datetime import datetime


# x = datetime.now()
# print(x)
# print(x.year)
# x = datetime(2023, 4, 25)
# print(x)
# print(x.strftime('%d of %B, %Y'))
# 25 of April, 2023

# txt = '2020-05-13 13:27:51'
# my_date = datetime.strptime(txt, '%Y-%m-%d %H:%M:%S')
# print(my_date)
# print(type(my_date))

# numbers = [34.6, -203.3, 44.9, 68.3, -12.2, 44.6, 12.7]
# numbers1 = [i for i in numbers if i > 0]
# print(numbers1)

# sentence = 'the quick brown fox jumps over the lazy dog'
#
# lenght = [len(word) for word in sentence.split() if word != 'the']
# print(lenght)

# def rank(lst, height):
#     for i in range(len(lst)):
#         if height >= lst[i]:
#             return i + 1
#     return len(lst) + 1
# print(rank = ([165, 163, 162, 160, 157, 157, 155, 154], 162))

# def rank(lst, height):
#     for i in range(len(lst)):
#         if height >= lst[i]:
#             return i + 1
#     return len(lst) + 1
#
# # print(rank([165, 163, 162, 160, 157, 157, 155, 154], 163))
# from datetime import datetime
# txt = '22_06_2021*13-45-16'
# p_date = datetime.strptime(txt, '%B %d, %Y, time: %H:%M:%S)
# print(p_date.strftime('%B %d, %Y, time: %H:%M:%S))


from datetime import datetime

txt = '22_06_2021*13-45-16'
p_date = datetime.strptime(txt, '%d_%m_%Y*%H-%M-%S')
print(p_date.strftime('%d_%m_%Y %H:%M:%S'))

