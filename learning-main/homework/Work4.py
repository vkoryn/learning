# my_list = [1, 'text2', False, 5.65, {1, 3}, (2,), {'key': 'value'}, [1, 'Test', True]]
# print(my_list[5])
# print(len(my_list))
# print('text2' in my_list)
# my_list.append(None)
# print(my_list)
# my_list[2] = True
# print(my_list)
# element_3 = my_list.pop(3)
# print(my_list, element_3)
# my_list.insert(6, 'triple_six_to_death')
# print(my_list, element_3)

# my_dict = {'name': 'John', 'second_name': 'Doe', 'age': 33}
# print(my_dict['age'])
# my_dict['name'] = 'Sarah'
# my_dict['middle_name'] = 'junior'
# my_dict.pop('age')
# dick = my_dict.pop('age')
# print(my_dict, dick)
# print(len(my_dict))
# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())

# my_tuple = (1, 'test', True)
# # my_tuple = (1,)
# print(my_tuple[1])

# my_set = {3, 1, 5, 7, 5}
# my_set.add(9)
# popped = my_set.pop()
# my_set.remove(5)
# print(my_set)
# my_list = [1, 3, 2, 3, 5, 1, 6, 3, 5]
# my_list = set(my_list)
# print(my_list)

# my_list = [1, 2]
# one, two = my_list
# print(one, two)

# my_list = {'admin': ('jon', 'doe'), 'user1': ('Hanna', 'M')}
# name, second_name = my_list['admin']
# print(name, second_name)


# my_list = ['text', {'name': 'viktar'}, 11, True]
# my_list2 = my_list[1:3]
# my_list3 = my_list[:3]
# my_list3 = my_list[2:]
# my_list3 = my_list[-3:]
# print(my_list3)

# my_string = 'some. text text text'
# print(my_string[2:])
# print(len(my_string))
# print('some' in my_string)
# my_list = my_string.split()
# my_list = my_string.split('.')
# my_list.reverse()
# my_string = ' '.join(my_list)
# print(my_string)

# my_string = 'This simple dUmMy texT'
# print(my_string.capitalize())
# print(my_string.title())
# print(my_string.upper())
# print(my_string.lower())

# my_string = '''"text1", text2, 'text3'''
# my_string = my_string.replace('"', "'")
# print(my_string)

# my_string = ' text '
# print('"' + my_string.strip() + '"')
# print('"' + my_string.lstrip() + '"')
# print('"' + my_string.rstrip() + '"')

# text = 'Current date {1} and time {0}'
# now = '13:21'
# day = 'Monday'
# print(text.format(now, day))

# color = 'green'
#
# if color.startswith('g'):
#     print('Is it grass?')
# elif color.startswith('y'):
#     print('Is it sun?')
# else:
#     print('Neither son nor grass')

# my_list = [1, 2, 3, 4, 5]
# for num in my_list:
#     if num <5:
#         print(num)

# my_dict = {
#     'name': 'john',
#     'second_name': 'Doe',
#     'height': 182,
#     'eyes': 'blue',
#     'weight': 75
# }
# for key, value in my_dict.items():
#     if key == 'weight':
#         print(value)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# i = 0
# while True:
#     print(i)
#     i += 1
#     if i > 20:
#         break

i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        continue
    print('test')
    if i > 20:
        break


test