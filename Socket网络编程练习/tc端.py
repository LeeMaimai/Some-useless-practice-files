from socket import *


IP = '127.0.0.1'
SERVER_PORT = 50000
BUFLEN = 512

dataSocket = socket(AF_INET,SOCK_STREAM)
#设置完客户端直接连接服务端socket

dataSocket.connect((IP,SERVER_PORT))

while True:
    toSend = input('>>> ')

    if toSend == 'exit':
        break

    dataSocket.send(toSend.encode())

    received = dataSocket.recv(BUFLEN)

    if not received:
        break

    print(received.decode())

dataSocket.close()
