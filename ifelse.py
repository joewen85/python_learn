# -*- coding: utf-8 -*-
#auther: Joe wen

num1 = input('number 1 is:')
num2 = input('number 2 is:')
#print(num1,'和',num2,'平均值：',(int(num1)+int(num2))/2)
age = int(input('input age:'))  #说明：如不变成int type会导致下面判断有问题，因为输入时是当作str type输入
# if num1 == num2:
#     print("num1 eq num2")
# else:
#     print("num1 ne num2")


if num1 == num2 and age == 2:
    print("num1 eq num2")
else:
    print("num1 ne num2")