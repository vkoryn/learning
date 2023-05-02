# from functools import reduce
#
# txt = 'abeehhhhhccced'
# #abe2h5c3ed
#
# def my_reduce(accum, char):
#     print(accum, char)
#
# reduce(my_reduce, txt)

# def my_func(x):
#     return x + 2
#
# fun_name = my_func
# print(fun_name(5))


# Функция my_func2 возвращает тело функции hello
# Результат вывода функции my_func3() - тело функции hello
# Для того, чтобы это тело было выполнено, нужно поставить дополнительные скобки или сохранить результат
# работы my_func3() в переменную и обратиться к переменной как к функции (т.е со скобками)
# # def my_func2():
# #     def hello():
# #         return 'hello'
# #     print(hello())
# print(my_func2())
# my_func2()()
# my_var = my_func2()
# print(my_var)
# my_var()


# Мы можем передать функцию на вход другой функции в качесте аргумента. В таком случае, можно будет
# использовать переданную функцию (simple) внутри функции получателя (my_func4)
# # def my_func4(func):
#     print('one')
#     func()
#     print('two')
#
# def simple():
#     print('simple')
#
# my_func4(simple)


# Символ @ используется для того, чтобы задекорировать какую-либо функцию.
# Таким образом, если перед функцией стоит main_func, то мы говорим, что саму функцию simple_func запускать
# не надо, но надо передать её на вход функции main_func
# def main_func(func):
#
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#
#     return wrapper
# @main_func
# def simple_func():
#     print('simple')
#
# simple_func  = main_func(simple_func)
# simple_func()

# def my_dec(func):
#
#     def wrapper(x, y):
#         print('wrapper')
#         func(x, y)
#
#     return wrapper
#
# @my_dec
# def calc(x, y):
#     print(x + y)
#
# calc(7, 3)

# def bread(func):
#     def wrapper():
#         print()
#         func()
#         print('<\__/>')
#
#     return wrapper
#
#
# def ingredients(func):
#     def wrapper():
#         print('#помидоры#')
#         func()
#         print('~салат~')
#
#     return wrapper
# @bread
# @ingredients
# def sandwich(food= '--ветчина--'):
#     print(food)
#
# sandwich()

# def my_dec1(func):
#
#     def wrapper(x):
#         x += 1
#         func(x)
#
#     return wrapper
#
# @my_dec1
# def fun1(x):
#     print(x)
#
# fun1(6)

# def upper_case_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
#
# @upper_case_decorator
# def sey_hello(name):
#     return f'Hello {name}!'
# print(sey_hello('alice'))

def change(func):

    def wrapper(*args):
        result = func(*args)
        return result[::-1]
    return wrapper

@change
def change1(a, b, c):
    return a, b, c
print(change1(1, 2, 3))



