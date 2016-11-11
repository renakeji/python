#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kn
# @Date:   2016-11-10 19:58:53
# @Last Modified by:   kn
# @Last Modified time: 2016-11-10 20:06:42
# 
# 1.
# 
# def make_incrementor(n):
#         return lambda x: x + n

# f = make_incrementor(42)
# print(f(1))

# 2.
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[0])
print(pairs) #[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
