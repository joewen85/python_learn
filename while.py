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

# s = 0
# number1 = ''
# while number1 != 0:
#     number1 = int(input("input nubmer is:"))
#     if number1 == 0:
#         break
#     s = number1+s
#     print(s)

# s = 0
# time = 0
# while True:
#     number1 = input("input number is: ")
#     if not number1.strip():
#         break
#     elif not number1.isdigit():
#         print("only support input number")
#     else:
#         time += 1
#         s = (int(number1)+s)/time
#         print(s)

balance = 10000
times = 0
while balance <= 20000:
    #balance = balance+balance*0.0325
    balance *= (1+0.0325)
    times += 1
print(times)