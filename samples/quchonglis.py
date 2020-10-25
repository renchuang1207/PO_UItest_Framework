#!/user/bin/env python
# encoding: utf-8
# @author: renchuang
# @file: quchonglis.py
# @time: 2020/10/23 6:54 下午


lis = [4,2,1,3,4,2,3,1,3,2,2,2]

# 解法1: 利用set去重，会改变列表顺序
lis1 = list(set(lis))
print(lis1)
# 解法2:
lis2 = []
for i in lis:
     if i not in lis2:
         lis2.append(i)
print(lis2)
