import socket
import sys

ClientSocket = socket.socket()
host = '192.168.56.105'
port = 8080

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    print ('\n Welcome to math calculator python ')
    print (' 1. Logarithmic ')
    print (' 2. Square Root ')
    print (' 3. Exponential ')
    print (' 4. Power ')
    print (' 0. Exit ')

    Input = input('Put number to choose type of calculation wanted: ')
    ClientSocket.send(Input.encode())

    if Input == '1':
        print ('\n [+] Log Function ')
        num = input('\n Enter Number : ')
        value = input('\n Enter base : ')
        ClientSocket.sendall(str.encode('\n'.join([str(num), str(value)])))
        total = ClientSocket.recv(1024)
        print ( ' Answer for log ' + num + ' base ' + value + ' : ' + str(total.decode()))

    elif Input == '2':
        root = True
        while root:
            print ('\n [+] Square Root Function ')
            num = input ('\n Enter Number : ')
            if float(num) <  0:
                print('\n Negative Number Cant Be Square Root')
            else:
                root = False
                ClientSocket.send(num.encode())
                total = ClientSocket.recv(1024)
        print ( ' Answer for sqrt ' + num +' : ' + str(total.decode()))

    elif Input == '3':
        print ('\n [+] Exponential Function ')
        num = input ('\n Enter Number : ')
        ClientSocket.send(num.encode())
        total = ClientSocket.recv(1024)
        print ( ' Answer for exp ' + num + ' : ' + str(total.decode()))

    elif Input == '4':
        print ('\n [+] Power Of Function ')
        num = input('\n Enter Number : ')
        val = input('\n Enter Power Of : ')
        ClientSocket.sendall(str.encode('\n'.join([str(num), str(val)])))
        total = ClientSocket.recv(1024)
        print ( ' Answer for ' + num + ' pow of ' + val + ' : ' + str(total.decode()))

    elif Input == '9':
        ClientSocket.close()
        sys.exit()

    else:
        print ('\n Invalid input please try again !')

    input( '\n Press Enter to Continue .. ')


