# -*- coding: utf-8 -*-
# @Author: renakeji
# @Date:   2016-11-10 11:45:35
# @Last Modified by:   renakeji
# @Last Modified time: 2016-11-10 14:46:51
#
# 1.
#
# words = ['cat','window','dog']
# for w in words:
#     print(w,len(w))
#
# 2.
# 不建议直接修改原序列
#
words = ['cat','window','insterting']
for w in words[:]:
    if len(w) > 5:
        words.insert(0,w)

print(words)