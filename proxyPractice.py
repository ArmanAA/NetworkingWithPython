import socket, sys
from _thread import *

host = socket.gethostname()
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET is an address family, which you have to specify while
#creating a socket. Sockets can only use the type of address you give them in order to communicate.
#SOCK_STREAM is a connection based protocal. When the two parties have a conversation, the connection is established.
try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))
s.listen(5)
print('Waiting for a connection...')

def threaded_client(conn):
    conn.send(str.encode('welcome, type your info\n'))
    while True:
        data = conn.recv(2048)
        reply = 'server output: '+ data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()
while True:
    conn, addr = s.accept()
    print('connected to: '+addr[0]+':'+str(addr[1]))

    start_new_thread(threaded_client, (conn,))




























