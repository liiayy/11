from socket import *
tcp_client_socket = socket(AF_INET, SOCK_STREAM)
server_ip = '62.234.156.248'
server_port = 1122
tcp_client_socket.connect((server_ip, server_port))
send_data = input("请输入要发送的数据：")
tcp_client_socket.send(send_data.encode("gbk"))
recvData = tcp_client_socket.recv(1024)
print('接收到的数据为:', recvData.decode('gbk'))
tcp_client_socket.close()