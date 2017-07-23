# -*- coding: utf-8 -*-
#auther: Joe wen

from socket import *
host = ''
port = 8899
address = (host,port)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(address)
serverSocket.listen(1)

while True:
    try:
        connectionSocket,clientAddr = serverSocket.accept() #获取套接字
        message = connectionSocket.recv(1024)   #获取http报文
        filename = message.split()[1]   #获得URI，去除首部'/'就是文件名
        f = open(filename[1:])

        outputdata = f.read()  #逐行读出文件内容并存到list中
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')    #发response行

        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata) #把文件各行数据塞到response中
        connectionSocket.close()    #关闭数据连接
    except IOError:
        connectionSocket.send("404 not found")  #文件不存在时异常处理
        connectionSocket.close()
serverSocket.close()
