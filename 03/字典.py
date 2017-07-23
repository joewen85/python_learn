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
content = ''.join(content.split())  #去除空格
#print(content)
res = {}
count = 0
for s in content:
    #res[s] = 0
    if s in res:
        res[s] +=1
    else:
        res[s] = count+1
print(res)

