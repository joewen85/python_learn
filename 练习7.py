# -*- coding: utf-8 -*-
#auther: Joe wen

while True:
    year = input("input number: ")
    if year.isdigit():
        if int(year)%100 == 0 and int(year)%400 == 0:
            print('%s is rui year' % (year))
        elif int(year)%4 ==  0 and int(year)>0:
                print('%s is rui year' %(year))
        else:
            print('%s is not rui year' %(year))
            continue
