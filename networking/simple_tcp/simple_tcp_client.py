import socket

#server hostname is the host address in which the server is running, the machine to which we want to connect to
server_hostname = "127.0.0.1"

#server port is the port number in which the server is running, the port to which we want to connect to
server_port = 14000

try:
    # Create a client socket object
    client_socket = socket.socket()
    # Connect  to the server socket after creating a socket object by binding the port and hostname
    client_socket.connect((server_hostname, server_port))
    # print the received message from server and decode into string as the message would be bytes
    print(client_socket.recv(1024).decode('utf-8'))
    # Messages sent via socket has to be bytes rather than string hence b"message"
    client_socket.send(b"Hi I am the client")
    # Be a dear and close the socket. The last thing we want is a socket open with no functionality
    client_socket.close()


except Exception as exception:
    #In case of exception close the socket
    client_socket.close()
    print(exception)