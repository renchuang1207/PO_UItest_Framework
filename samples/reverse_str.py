#!/user/bin/env python
# encoding: utf-8
# @author: renchuang
# @file: reverse_str.py
# @time: 2020/10/25 11:52 下午

#第一种方法，不使用任何系统，且时间复杂度小
def reverse_str(input_str):
	ch = list(input_str)#强转为list
	lens = len(ch)
	i=0
	j=lens-1
	while i<j:
		tmp = ch[i]
		ch[i] = ch[j]
		ch[j] = tmp
		i+=1
		j-=1
	return ''.join(ch)

# print(reverse_str('nihao'))

#第二种，使用切片
def reverse_str_002(input_str):
	result = input_str[::-1]
	return result

print(reverse_str_002('nihao'))

#第三种方法，使用列表的reverse方法

def reverse_str_003(input_str):
	l = list(input_str)
	l.reverse()
	result = "".join(l)
	return result

print(reverse_str_003('nihao'))






