__author__ = 'cao'
# coding:utf-8
import json

file = open("result.txt", 'r', encoding='utf-8')
lines = file.readlines()
jsonStr = ''.join(lines)
jsonArray = json.loads(jsonStr)

for ele in jsonArray:
    print(ele)