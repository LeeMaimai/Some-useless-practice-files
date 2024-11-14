from socket import *
#定义ip地址，端口号，一次从缓冲区最多读取512字节数据
IP = '127.0.0.1' # 如果所有ip都能连，就是0.0.0.0，如果需要指定的ip能连，就输入指定的公网ip
PORT = 50000
BUFLEN = 512

# AF_INET表示网络层使用的是IP协议
# SOCK_STREAM,stream是流的意思，相当于传输层用的tcp协议
# listenSocket是用来监听
listenSocket = socket(AF_INET,SOCK_STREAM)
# 绑定地址和端口
listenSocket.bind((IP,PORT))
# 使socket处于监听状态，等tc来连接,5表示接受多少个等待连接的客户端
listenSocket.listen(5)
print(f'服务端启动成功，在{PORT}端口等待客户端连接')
#datasocket是新产生的，用来传输数据的，addr告诉客户端用的ip和端口
dataSocket,addr = listenSocket.accept()
print('接受一个客户端连接：',addr)

while True:
    # 这里recv的是字节串不是字符串
    received = dataSocket.recv(BUFLEN)
    # 如果返回的是空bytes，说明对方关闭了连接
    if not received:
        break
    # 把字节数据解码成字符串
    info = received.decode()
    print(f'收到对方信息:{info}')
    # 发送的类型是bytes，所以要编码
    # 演示方便理解，我们把收到的消息再编码发回去
    dataSocket.send(f'服务端收到了信息{info}：'.encode())

dataSocket.close()
listenSocket.close()
