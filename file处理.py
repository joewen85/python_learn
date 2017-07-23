# -*- coding: utf-8 -*-
#auther: Joe wen
phone_list = []
user_list = []
passwd_list = []
f = open('user.txt','r')

_usernphone = input('input username or phone number :')
#_phonenum = input('input phone :')
_passwd = input('input password :')
user_exist = False
for i in f:
    temp = i.strip().split(':')
    # phone_list.append(temp[0])
    # user_list.append(temp[1])
    # passwd_list.append(temp[2])
    #print(temp)
if temp[0] == _usernphone or temp[1] == _usernphone:
    if _passwd == temp[2]:
        print('login succeed')
        user_exist = True
    else:
        print('password error')
        exit()
else:
    print('username or phone number error')
    exit()
f.close()
if not user_exist:
    print('user not exist')
