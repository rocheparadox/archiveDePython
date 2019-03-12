import socket
import sys

sock = socket.socket()
ip = "192.168.241.254"
port = 11000

args = sys.argv
port = int(args[1])


while True:
    try:
        sock.connect((ip,port))
        dataBytes = sock.recv(1024)
        data = dataBytes.decode("utf-8")
        print(data)
        dataToSend = (input("-->"))
        sock.send(bytes(dataToSend,"utf-8"))
        dataBytes = sock.recv(1024)
        data = dataBytes.decode("utf-8")
        print(data)
        sock.close()
        connectA = input("Connect Again??")
        if(connectA == "no"):
            break
    except Exception as e:
        print(e)
        print("Server is not available")
        connectA = input("Try Again??")
        if(connectA == "no"):
            break
        

