# -*- coding: utf-8 -*-
# #auther: Joe wen
# i = 0
# while i < 20:
#     print(i)
#     i += 1  #这里相当于i = i+1
#
#
# name = ''
# while not name:
#     name = input("input name is: ")
# print('my name is:',name)

s = 0
number1 = ''
while number1 != 0:
    number1 = int(input("input nubmer is:"))
    if number1 == 0:
        break
    s = number1+s
    print(s)