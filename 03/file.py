# -*- coding: utf-8 -*-
#auther: Joe wen

# f = open('user.txt','w+')
# f.write('hello world\n')
#
# #writelines传一个list到文件里，会合并到同一行，如果想换行，必须自己加\n换行符
# f.writelines(['xxx','ddd'])
# f.writelines(['xxx\n','ddd'])
# f.close()

username = input('input username:')
password = input('input password:')
accout = {}
f = open('user.txt','r+')
for i in f:
#     username_list = i.split(':')
# if username == username_list[0]:
#     print('用户已存在')
# else:
#     f.writelines('\n')
#     f.writelines([username,':',password])
    username_list = i.strip().split(':')
    print(username_list)
    accout[username_list[0]] = username_list[1]
# a = eval(accout)
# print(a)

accout.get(username,f.writelines(['\n',username,':',password]))
f.close()