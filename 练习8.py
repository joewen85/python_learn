# -*- coding: utf-8 -*-
#auther: Joe wen

list = ['C','js','python','js','css','js','html','node','C','js','python','js','css','js','html','node']

a = {}
for i in list:
    if list.count(i)>1:
        a[i] = list.count(i)
print(a)