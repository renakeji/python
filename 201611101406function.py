# -*- coding: utf-8 -*-
# @Author: renakeji
# @Date:   2016-11-10 14:06:13
# @Last Modified by:   renakeji
# @Last Modified time: 2016-11-10 14:46:41
#
# 1.
# 函数如果没有输出的话，会输出None,使用print()可以看到
#
# def fib(n):
#     """Print a Fibonacci series up to n."""
#     a,b = 0,1
#     while a < n:
#          print(a,end=' ')
#          a,b = b,a+b
#     print()

# a = int(input('input a num :'))

# fib(a)
#
# 2.带表达式的return
#
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result

s=int(input('input a integer :'))
f100 = fib2(s)
print(f100)
