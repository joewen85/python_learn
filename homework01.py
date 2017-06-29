# -*- coding: utf-8 -*-
#auther: Joe wen
#求list序列中最大的两个数

list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
#利用list排序方法实现
# list.sort(reverse=True)
# print(list[0],list[1])

#利用for循环实现
max_a = 0
max_b = 0
for i in list:
    if i > max_a:
        temp = max_a
        max_a = i
    elif i > max_b:
        max_b = i
print(max_a,max_b)


