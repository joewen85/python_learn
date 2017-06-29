# -*- coding: utf-8 -*-
#auther: Joe wen

# arr = [1,2,3,'hello','world',True,False,[1,2,3,[5,6,7]]]
# print(arr[0])
# print(arr[5])
# print(arr[-1])
# print(arr[-3])
# for i in arr:
#     print(i)

# num_arr = [1,2,3,4,5,6,7,8,9]
# for i in num_arr:
#     temp = ' '
#     for j in num_arr:
#         if j<=i:
#             temp += '%s*%s = %s ' %(i,j,i*j)
#     print(temp)

# print(list('hello'))
# #判断某元素师傅在list里
# print('h' in list('hello'))
# print('x' in list('hello'))
#
# #len函数，可以知道list中的长度
# print(len([1,2,3,4,5,6]))
#
# #数组拼接
# print([1,2,3]+[4,5,6])
#
# #修改该，直接查找在修改该。
# arr = [1,2,3]
# arr[0] = 9
# print(arr)


arr = [1,2,4,5,7,10,11,123,555,666,888,1000,2000,300000,400000]
number = int(input('input number is: '))
if number in arr:
    print('the number in arr list, number is %s' %(number))
else:
    print('input number not exist')