# -*- coding: utf-8 -*-
#auther: Joe wen

# for i in ['aa','bb','cc']:
#     print(i)
#
# for num in range(0,20):
#     print(num)

# times = 0
# for i in ['C','js','python','js','css','js','html','node']:
#     if i == 'js':
#         times += 1
# print(times)

#可以用列表排序来写，也可以用for迭代方式，将list里面的元素进行比较。取大数
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,44,555,666,65555,332,444,22252]
# list.sort(reverse=True)
# print(list[0])
s = 0
for i in list:
    if i > s:
        s = i
print(s)