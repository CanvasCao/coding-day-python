__author__ = 'cao'
# coding:utf-8


format = 'select * from table_student where age=%d and name=%s'
values = (18, 'Alex')
sql=format%values

print(sql)