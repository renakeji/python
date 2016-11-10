# -*- coding: utf-8 -*-
# @Author: renakeji
# @Date:   2016-11-10 11:42:04
# @Last Modified by:   renakeji
# @Last Modified time: 2016-11-10 11:44:09
x = int(input("Please enter an integer:"))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('single')
else:
    print('more')
