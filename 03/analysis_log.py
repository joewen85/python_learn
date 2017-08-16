# -*- coding: utf-8 -*-
#auther: Joe wen

ips_dict = {}

with open("access_log",'r') as f:
#     for i in f:
#         #dict_key必须是tuple,key不可变。
#         dict_key = (i.split()[0],i.split()[8])
#         ips_dict[dict_key] = ips_dict.setdefault(dict_key,0) + 1
#
# #利用sorted函数，按value值进行排序。sorted(iterable,key,reverse)。要跟可迭代对象，key参数对应的是=隐式函数lambda x:y。x表示输出的参数，y表示lambda
# new_list = sorted(ips_dict.items(),key=lambda item:item[1],reverse=True)
#
# h = open("show.html",'w')
#
# h.write('''
#  <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
#     <table border="1">
#         <tr><td>rank</td><td>ip</td><td>status</td><td>times</td></tr>\n''')
# for k in range(10):
#         content_add = '''
#         <tr>
#             <td>%s</td>
#             <td>%s</td>
#             <td>%s</td>
#             <td>%s</td>
#         </tr>
#         '''%(k + 1,new_list[k][0][0],new_list[k][0][1],new_list[k][1])
#         h.write(content_add)
# h.write('''</table>
# </body>
# </html>''')
# h.close()

# {
#     ip1:{
#         200:1
#     }
# }
    res_dict = {}
    for line in f:
        temp = line.split()
        ip = temp[0]
        status = temp[8]
        if ip in res_dict:
            if status in res_dict[ip]:
                res_dict[ip][status] += 1
            else:
                res_dict[ip][status] = 1
        else:
            res_dict[ip] = {status:1}
    #print(res_dict)
for ip in res_dict:
    for statue in res_dict[ip]:
        print(ip,status,res_dict[ip][statue])
