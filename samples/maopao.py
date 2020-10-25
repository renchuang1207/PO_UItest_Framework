#!/user/bin/env python
# encoding: utf-8
# @author: renchuang
# @file: maopao.py
# @time: 2020/10/23 5:54 下午

def bubble_sort(lists):
	'''
		冒泡排序（升序）【稳定排序】
		原理：
		1、从第一个元素开始，开始依次对相邻的两个元素进行比较，当后面的元素大于前面的元素时，交换二者位置；
		2、进行一轮比较之后，最大的元素将在序列尾部（最后一位）；
		3、然后对（n-1）个元素再进行第二轮比较，最大元素将在序列倒数第二位；
		4、重复该过程，直至只剩下最后一个元素为止，最后的元素就是最小值，排在序列首位
	
		以 list = [5, 4, 2, 1, 3] 为例：
		第一轮排序: [4, 2, 1, 3, 5]
		第二轮排序: [2, 1, 3, 4, 5]
		第三轮排序: [1, 2, 3, 4, 5]
	
		时间复杂度：O(n) ~ O(n**2)  平均：O(n**2)
		空间复杂度：O(1)
	
		:param lists:
		:return lists:
		'''
	for i in range(len(lists) - 1):
		for j in range(len(lists) - i - 1):
			if lists[j] > lists[j + 1]:
				lists[j], lists[j + 1] = lists[j + 1], lists[j]
	return lists

# 调用冒泡排序
bubble_sort_list = bubble_sort([5, 4, 2, 1, 3])
print(bubble_sort_list)