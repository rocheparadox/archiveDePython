import socket

#hostname of the server - Receiver's apartment in out analogy
server_hostname = "127.0.0.1"
#port of the server - Receiver's flat number in out analogy
server_port = 14000

try:
    server_sock = socket.socket()
    # Bind the server's hostname and port to create a socket object
    server_sock.bind((server_hostname, server_port))
    # Tell the system to listen to the port in the hostname. A maximum of 5 connections can be handled simulataneously
    server_sock.listen(5)
    while True:
        client_sock_obj, client_addr = server_sock.accept()
        # print the hostname and port of the client which connects to the server
        print("Got connection from client " + str(client_addr))
        # send a short message to the client
        # Messages sent via socket has to be bytes rather than string hence b"message"
        client_sock_obj.send(b"Hi am the server")
        # print the received message from server and decode into string as the message would be bytes
        print(client_sock_obj.recv(1024).decode('utf-8'))
        # Close the connection with client_sock_obj cuz our business with that client socket object is done.
        client_sock_obj.close()


except KeyboardInterrupt:
    print("Server stopped")
    # Close the server socket object gracefully
    server_sock.close()

except Exception as exception:
    print(str(exception))
    # Close the server socket object gracefully
    server_sock.close()









