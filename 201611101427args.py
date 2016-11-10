# -*- coding: utf-8 -*-
# @Author: renakeji
# @Date:   2016-11-10 14:27:36
# @Last Modified by:   renakeji
# @Last Modified time: 2016-11-10 14:59:33
#
# 1.多参数
#
# def ask_ok(prompt,retries=4,complaint='Yes or no,please!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y','ye','yes'):
#             return True
#         if ok in ('n','no','nop','nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise OSError("uncooperative user")
#         print(complaint)

# ask_ok('Do you want to quit?',2)
#
# 2.默认值只赋值一次
#
# def f(a,L=[]):
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))

# def f1(a,L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f1(1))
# print(f1(2))
# print(f1(3))
#
# 3.关键字参数
#
# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
#
# 4.元组，字典参数
#
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    # keys = keywords.keys() # 打印顺序随机
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")