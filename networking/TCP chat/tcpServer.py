import socket
import sys
sock = socket.socket()
ip = "172.24.124.99"
#ip = "172.22.159.239"
port = 40000

args = sys.argv
try:
	port = int(str(args[1]))
except:
	pass
print("Server up at " + ip +" " + str(port)  )
sock.bind((ip,port))
sock.listen(5)

while True:
    try:
        closeServer = input("Close Server? ")
        if(closeServer == "yes"):
            sock.close()
            break
        clientSock,clientAddr = sock.accept()
        print("Got connection from " + str(clientAddr))
        clientSock.send(bytes("Hello.. Whats up?","utf-8"))
        dataBytes = clientSock.recv(1024)
        data = dataBytes.decode("utf-8")
        print(data)
        dataToSend = (input("-->"))
        clientSock.send(bytes(dataToSend,"utf-8"))
        clientSock.close()
    except Exception as e:
        print(e)
