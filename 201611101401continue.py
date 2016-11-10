# -*- coding: utf-8 -*-
# @Author: renakeji
# @Date:   2016-11-10 14:01:37
# @Last Modified by:   renakeji
# @Last Modified time: 2016-11-10 14:04:50
#
for num in range(2,10):
    if num % 2 == 0:
        print('Found an even number ',num)
        continue
    print('Found a number ',num)