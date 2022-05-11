# import union as union
# even = 'Hand on the floor'
# new_stroke = ''
# i = 1
#
# for char in even:
#     if i % 2 == 1:
#         char = '_'
#     elif i % 2 == 0 and char == 'a':
#         char = 'b'
#     i += 1
#     new_stroke += char
#
# # me = list(['d', 'o', 'v', 'o', 'd', 'i'])
# # print(me)
# # mo = list()
# # for index in range((len(me) - 1), -1, -1):
# #     mo.append(me[index])
# # print(mo)
# # if me == mo:
# #     print("It is paraloid")
# # else:
# #     print("It's not palindrom")
# # print([1, 2, 3, 4, 5][1: 125])
# #
# # d = {'a': -5, 'b': 'hello', 'c': 4, 'd': -3}
# # maks = d['a']
# # for key, value in d.items():
# #     if type(d[key]) is int:
# #         if maks < value:
# #             maks = value
# # print(maks)
#
#
# def maximus(*args):
#     for i in args:
#         try:
#             if type(i) is int:
#                 pass
#             else:
#                 raise TypeError
#             return max(args)
#         except TypeError as e:
#             return print('Список має не тільки числа. ', e)
#
#
# sir = maximus(1, 2, 4, 6, -6, 124)
# print(sir)
#
# def nsk(first_num, second_num):
#     list_nsk = list()
#     if first_num < second_num:
#         for i in range(1, first_num + 1):
#             if (first_num % i == 0) and (second_num % i == 0):
#                 list_nsk.append(i)
#     else:
#             for i in range(1, second_num + 1):
#                 if (first_num % i == 0) and (second_num % i == 0):
#                     list_nsk.append(i)
#     return max(list_nsk)
# ns = nsk(150, 100)
# print(ns, end='xuy')
# print('marko nhbn ')
#
# set_a = {1, 2, 3}
# set_b = {4, 5, 6}
# print(set_a.union(set_b))
# ni = 'FHBVDGF'
# no = 'Fghkjj'
# print(no == ni)
#
# a = 10
# b = 5
#
# for i in range(0, 11, 2): print(i)
#
#
# def check_pow_2(n):
#     if n == 1:
#         print("Yes")
#     else:
#         if n % 2 == 0:
#             check_pow_2(n // 2)
#         else:
#             print("NO")
#
# check_pow_2(6)
# user = {'name': "JohnDoe",
#         'info': {
#             "basic": {
#                 'age': 25,
#                 'salary': 5000
#             },
#             'additional': {
#                 'study': 'mathematics',
#                 'family': 'married'
#             },
#             'special': {
#                 'projects': [
#                     {'name': 'quantum computer', 'stage': 'in-process'},
#                     {'name': 'laser-gun', 'stage': 'in-production'}
#                 ]
#             }
#         }
#         }
#
#
# def get_data(data_dict, keys):
#     data = data_dict
#     for key in keys:
#         data = data[key]
#     return data
#
#
# def get_data_rec(data_dict, keys, index=0):
#     if index < len(keys):
#         return get_data_rec(data_dict[keys[index]], keys, index + 1)
#     return data_dict
#
# # print(get_data(user, ['info', 'special', 'projects']))
# print(get_data_rec(user, ['info', 'special', 'projects', 0, 'name']))
# def function(index, count):
#     data = {"ID": index,
#             "values": ['{}_{}'.format(value, index) for value in range(count)]
#             }
#     return data
#
#
# def generate_list(count):
#     return [function(i, j) for i, j in zip(range(count), list(range(count)[::-1]))]
#
#
# print(function(1, 5))
# print(generate_list(5))
# r = generate_list(10)
# f = [val for sublist in r for val in sublist['values']]
# print(f)
import math
import collections
print('Hello world')
hero = [
    {'hp': 100, 'mana': 300, 'stamina': 50},
    {'name': 'Jonathan', 'surname': 'Sairus', 'age': 22},
    {'type': 'wizard', 'weapon': 'staff', 'main_spell': 'meteor'}
]

def get_data(data, keys):
    dete = data
    for key in keys:
        dete = dete[key]
    return dete

print(get_data(hero, [1, 'name']))
print(hero[1]['name'])
a = math.ex
print(a)