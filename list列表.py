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

#用户输入数字，如何最快的找到用户输入数字的索引
# arr = [1,2,4,5,7,10,11,123,555,666,888,1000,2000,300000,400000]
# number = int(input('input number is: '))
# start = 0
# end = len(arr)-1
# while True:
#     mid_index = int((start+end)/2)
#     mid_num = arr[mid_index]
#     if number < mid_num:
#         #print(mid_num)
#         end = mid_index
#     elif number > mid_num:
#         #print(mid_num)
#         start = mid_index
#     else:
#         print('find the number: %s' %(mid_index))
#         break

# #数组切片
# arr = [1,2,3,4,5,6,7,8,9]
# print(arr[1:3])
# print(arr[1:])
# print(arr[:])
# print(arr[::-1])

#arr = [3,7,18,2,20,99,1,54]
# arr[1:1] = [6]
# print(arr)
# arr[2:5] = []
# print(arr)

#冒泡算法
# arr = [1000,3,10000,999,7,18,2,20,99,1,54,11,111,1235,566,7878,554554]
# leng = len(arr)
# max_number = 0
# #print(leng)
# #相邻对比，大的往右移，依次向下比
# # for j in range(leng):
# #     next_num = (arr[j])
# #     #print(next_num)
# #     for i in arr:
# #         if i > next_num:
# #             i,next_num = next_num,i
# #             break
# # print(arr)
# count = 0
# for j in range(arr):
#     for i in range(leng-1):
#         if arr[i] > arr[i+1]:
#             count += 1
#             arr[i],arr[i+1] = arr[i+1],arr[i]
# print(count)
# print(arr)

#数组中去重
# arr = [1,2,3,1,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,411,22,333,4]
# new_arr = []
#
#
# for i in arr:
#     if i not in new_arr:    #利用in，i是否在新的列表中，因new_arr为空，所以循环arr数组中的重复数就不会append到new_arr中
#         new_arr.append(i)
# print(new_arr)
#
# #利用集合实现去重功能
# new_arr = list(set(arr))
# print(set(arr))
# print(new_arr)


#求两个数组共同的值（去重）
# arr1 = [1,2,3,1,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,411,22,333,4]
# arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
# #利用集合的交集实现
# n_arr1 = set(arr1)
# n_arr2 = set(arr2)
# #print(n_arr1,n_arr2)
# print(n_arr1&n_arr2)
#
# new_arr = []
# for i in arr1:
#     # if i in arr2:
#     #     if i not in new_arr:
#     #         new_arr.append(i)
#     if i in arr2 and i not in new_arr:
#         new_arr.append(i)
# print(new_arr)


#字符串

#split把字符串切割为list
# print('hello,joe,world'.split(','))
#
# #join把list拼接成字符串
# print(','.join(['hello','joe','world']))
#
# #replace
# print('hello,world'.replace(',','|'))
#
# my_str = 'hello,reboot:you,xxx,xxx:xxx'
# new_str = my_str.replace(':',',')
# print(new_str.split(','))

arr = ['user:pwd','user1:pwd1','user2:123']

# my_str = ','.join(arr)
# #print(my_str)
# mylist = my_str.split(',')
# print(mylist)
# user2pwd = input('username and password(user:password) :')
# if user2pwd in mylist:
#     print('login succeed')
# else:
#     print('login fail')
user = input('input user name : ')
pwd = input('input password : ')
user_list = []
pwd_list = []

for i in arr:
    temp = i.split(':')
    print(temp)
    user_list.append(temp[0])
    pwd_list.append(temp[1])

if user in user_list:
    if pwd == pwd_list[user_list.index(user)]:
        print('succeed')
    else:
        print('password wrong')
else:
    print('user not exist')