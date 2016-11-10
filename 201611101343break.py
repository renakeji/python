# -*- coding: utf-8 -*-
# @Author: renakeji
# @Date:   2016-11-10 13:43:34
# @Last Modified by:   renakeji
# @Last Modified time: 2016-11-10 14:46:39
#
# 1.break 跳出最近的循环,else 为第二个for的结构，当for执行完毕都未执行if时，则执行else

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,' equals ',x,' * ',n/x)
            break
    else:
        print(n,' is a prime number')