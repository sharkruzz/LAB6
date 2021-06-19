import socket
import sys
import math
import errno

from multiprocessing import Process

def process_start(s_sock):

    while True:
        choice = s_sock.recv(1024).decode()

        if choice == '1':
            num,value = [float(i) for i in s_sock.recv(2048).decode('utf-8').split('\n')]
            calc = math.log(float(num),float(value))

        elif choice == '2':
            num = s_sock.recv(1024).decode()
            calc = math.sqrt(float(num))

        elif choice == '3':
            num = s_sock.recv(1024).decode()
            calc = math.exp(float(num))

        elif choice == '4':
            num, val = [float(i) for i in s_sock.recv(2048).decode('utf-8').split('\n')]
            calc = math.pow(num,val)

        elif choice == '0':
            s_sock.close()
            break

        s_sock.sendall(str(calc).encode())

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 8080
    print("listening...")

    try:
        s.bind((host,port))
    except socket.error as e:
        print(str(e))
        sys.exit(0)

    s.listen(5)
    while True:
            try:
                s_sock, s_addr = s.accept()
                print('successfully connected')
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:
                print('got a socket error')
    s.close()
