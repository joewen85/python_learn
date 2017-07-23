# -*- coding: utf-8 -*-
#auther: Joe wen

#1.冒泡排序算法，与相邻比较，将最大的数排到最右边
arr = [1,2,3,4,555,666,888,333,999,22222,44,56,87]

long = len(arr)
#print(long)
count = 0
for i in range(0,long):
    for j in range(i+1,long):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        count +=1
print(arr)
print(count)