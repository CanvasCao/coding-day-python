import copy

__author__ = 'cao'
# coding:utf-8


list1 = [1, 2]
list2 = copy.deepcopy(list1)
list2[0] = 3
print(list1)
print(list2)