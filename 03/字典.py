# -*- coding: utf-8 -*-
#auther: Joe wen

# #字典 = （其他语言里，这正数据结构叫做哈希表）
#
#
# #字典里的数据没有顺序，是key:value的形式，key必须是不可变的数据结构，value任意
# mydict = {
#     'a':1,
#     'b':2,
#     'age':12,
#     ('ttt'):10,
#     'des':{
#         'job':'ops',
#         'company':'gdxh'
#     }
#     }
# print(mydict)
# print(mydict['age'])
# print(mydict[('ttt')])
# print(mydict['des']['job'])
#
# #修改：
# mydict['age'] = 13
# print(mydict)
#
# #添加
# mydict['name'] = 'joe'
# print(mydict)
#
# #删除
# del mydict['a']
# del mydict['b']
# print(mydict)
#
# #in判断字典里是否存在key
# print('age' in mydict)
# print('abc' in mydict)
#
# #for循环遍历dict
# for k in mydict:
#     print(k,mydict[k])

content='''first of all, i wantiiiiiiiiii make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!'''
# 字符:次数
# content = ''.join(content.split())  #去除空格
# #print(content)
# res = {}
# numb = []
# count = 0
# for s in content:
#     #res[s] = 0
#     if s in res:
#         res[s] +=1
#     else:
#         res[s] = count+1
# print(res)
#
# #将结果，打印前10名
# import operator
# res_list = []
# new_dict = {}
# for k in res:
#     res_list.append([k,res[k]])
# res_list.sort(key=operator.itemgetter(1),reverse=True)
#
# #转换为list后，使用冒泡排序
# # for i in range(10):
# #     for n in range(len(res_list)-1):
# #         if res_list[n][1] > res_list[n+1][1]:
# #             res_list[n],res_list[n+1] = res_list[n+1],res_list[n]
# # for r in res_list[-10:]:
# #     print('string is %s:%s'%(r[0],r[1]))
# # print(res_list)
# #将list传入dict（）函数中，让它来处理
# new_dict = dict(res_list[0:9])
#
# #遍历方式将嵌套list转为字典
# for l in res_list[0:9]:
#     new_dict[l[0]] = [l[1]]
# print(new_dict)

#简单方法：
# res = {}
# for s in content:
#     res[s] = res.get(s,0)+1 #使用get方法，如果res中无s变量的值，则默认为0，如果res中存在s变量的值res[s]+1
#     # if s == ' ':
#     #     continue
#     # if s in res:
#     #     res[s] += 1
#     # else:
#     #     res[s] = 1
# print(res)



#简单的数据结构赋值给别的变量时，是复制一份，两个变量没有关系，简单数据结构包括数字、字符串、布尔,专业词汇叫值传递
# name = 'joe'
# my_name = name
# my_name = 'may'
# print(name)
#
# #复杂的数据结构，元祖、列表、字典赋值，是把内存地址赋值，值是共享一份，所以修改一份全部会影响，专业词汇叫引用传递
# d = {'a':1}
# my_dict = d
# my_dict['a'] = 3
# print(d)
#
# #判断name是否存在字典里，存在就打印，使用get方法
# a = {'name1':'xxx'}
# if 'name' in a:
#     print(a['name'])
# else:
#     print('no')
#
# #使用get方法简单得多
# print(a.get('name1','no'))

#fromkeys快速从list转成一个dict

print({}.fromkeys(['name','age'],'xxx'))


# my_dict = {'name':'joe','age':'30'}
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

#popitem 从dictz随机里弹出值
my_dict = {'name':'joe','age':'30'}
print(my_dict.popitem())

#setdefault 设置默认值，和get类似。判断如果key不存在，默认值就是abab
my_dict = {'name':'joe','age':'30'}
my_dict.setdefault('name1','abab')  #key中没有name1，所以在原字典中添加name1：abab
print(my_dict)

#read方法读取文件固定长度的字符，不传读取所有
#所有操作文件的方法，都是一个文件指针概念 每次read都会修改文件指针位置，下次read从指针位置开始
f = open('../user.txt')
# print(f.read(5))
# print(f.read(5))
# print(f.read())

print(f.readline()) #每次只读一行
print(f.readlines())    #一次全部读完，返回一个list,每行一个元素
f.close()
