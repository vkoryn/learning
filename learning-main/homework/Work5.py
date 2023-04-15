# i = 0
# while i < 10:
#     if i == 10:
#         break
#     else:
#         print(i)
#     i += 1

# i = 2.3434535435
# print(round(i, 2))

# i = -1
# print(abs(i))

# import random
# print(random.random())
# print(random.randint(1, 10))
# value = ['this', 'is', 'my', 'test']
# print(random.choice(value))
# print(random.randrange(1, 100, 5))

# import math
# print(math.sqrt(9))

s = 'ewfewwfhiewfuhiwehfwef'
# print(s[0:5:2])
# print(s[5:0:-2])
# print(s[::-1])
# print(s.count('w'))
# print(s.find('fuh'))
# print(s.index('fuh'))

# l1 = ['bla', 'qqq']
# l2 = l1.copy()
# l1.append('pop')
# print(l1, l2)

# s = 'hello' * 100
# print(s)
# l = [False] * 10
# print(l)

# i = 1
# i += 1
# print(i)

# s1 = 'Viktar'
# s2 = s1 + ' Koryn'
# print(s2)

# l = [1, 5, 3, 2]
# # l.sort()
# l.sort(reverse=True)
# print(l)

# l = [1, 5, 3, 2]
# print(min(l))
# print(max(l))
# print(sum(l))

l = [1, 5, 3, 2]
# for i in enumerate(l):
#     print(i)
# for index, value in enumerate(l):
#     if index % 2 == 0:
#         print(f'index is {index}, value is {value}')

# for i in range(0, 10):
#     print(i)

# s = ''
# l = 1
# d = None
# if s:
#     print("isn't true")
#
# l = ['test', 0, True]
# print(any(l))

# second_names = ['petrov', 'ivanov', 'sidorov', 'lennon', 'bach']
# second_names.sort()
# for i in second_names:
#     print(i)

# second_names = ['petrov', 'ivanov', 'sidorov', 'lennon', 'bach']
# second_names.sort()
#
# for name in second_names:
#     name_with_dashe = '-'.join(name)
#     print(name_with_dashe)

# a = 2
# b = 2
# if a > b:
#     c = a - b
#     print(c)
# elif a < b:
#     c = a + b
#     print(c)
# elif a == b:
#     c = a
#     print(c)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total)

my_list = ['a', 'b', 'c']
new_list = []
for i, v in enumerate(my_list):
    new_list.append(f'{i+1}: {v}')
print(new_list)
