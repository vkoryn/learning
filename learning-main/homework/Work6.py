# def f_name(x, y):
#     result = x + y
#     return result
#
# print(f_name(4, 6))

# def f_name(x, y=4):
#     result = x + y
#     return result
#
# print(f_name(4))

# def f_name(x, y=4):
#     result = x + y
#     return result
#
# print(f_name(y=4, x=2))
#
# def f_name(x, y=4):
#     result = x + y
#
# print(f_name(3, 2))

# def f_name(x, y=2):
#     if not isinstance(x, int):
#         return 0
#     return x + y
#
#
# print(f_name({}, 2))

# def f_name(x, y=2):
#     if not isinstance(x, int):
#         return 'Not int'
#     return x + y, x * y
#
# res1, res2 = f_name(3, y=2)
# print(f'res1: {res1}, res2: {res2}')

# def f_name(*my_args):
#     # print(my_args)
#     for arg in my_args:
#         print(arg)
#     return sum(my_args)
#
# print(f_name(1, 4, 3, 5, 7))

# def f_name(name, second, **my_kwargs):
#   '''school, class, weight, height, eyes'''
#   text = f'Name is {name}, second name is {second}'
#   if 'eyes' in my_kwargs:
#       text += f' and eyes are {my_kwargs["eyes"]}'
#   return text
#
#
# print(f_name(name = 'John', second = 'Smith', eyes = 'grey'))

# l1 = [i for i in range(1, 10)]
# bbb = [10, 20, 37]
# # l1 = [i * 3 for i in bbb]
# l1 = [i * 3 for i in bbb if i % 2 == 0]
# print(l1)

# d = {i: i+10 for i in range(1, 10)}
# print(d)

# l = ['dqwd', 'wvwv', 'qeewrt']
# d = {k: v for k, v in enumerate(l) }
# print(d)


# def f_name(x, y):
#     result = x + y
#     return result
#
#
# print(f_name('Hello ', 'World'))

# В идеале решение такое

# def hello():
#     return 'Hello world!'
# print(hello())

# def f_name(x, y, c):
#     result = x + y + c
#     return result
#
# print(f_name(4, 6, 5))

# l1 = ()
# def f_name(x, y):
#     l1 = x - y
#     if l1 < 0:
#         return 'Wrong'
#     return str(l1)[::-1]
#
#
# print(f_name(2, 11))

# def f_name(x):
#     if str(x)[::1] == str(x)[::-1]:
#         return True
#     else:
#         return False
#
#
# print(f_name('lola'))
l1 = ['old', 'Pil', 'Afrian']
l2 = ['African', 'Roman Tufted', 'Toulouse', 'Pilgrim', 'Steinbacher']
def f_new(x,y):
    for elem in l2:
        if elem in l1:
            l1.remove(elem)
    return l1
print(f_new((l1), (l2)))