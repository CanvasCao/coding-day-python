__author__ = 'cao'
# coding:utf-8

class SherryModule():
    name = 'Sherry'

    @staticmethod
    def isHui(s):
        list1 = (list(s))
        list1.reverse()
        return s == (''.join(list1))
