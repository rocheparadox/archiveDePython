#Author : Roche Christopher
#File created on 29 Jan 2020 4:04 PM

import socket
import sys, os

def is_host_alive(hostname):

    response = os.system("ping -c 1 " + hostname)

    # and then check the response...
    if response == 0:
        return True
    else:
        return False


if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = input("Enter the host name or IP address:")

if not is_host_alive(host):
    print("Host is not pingable")
    exit()

sock = socket.socket()
for port in range(1,65535):

    sys.stdout.write("Checking port {} \r".format(port))
    sys.stdout.flush()

    try:
        sock.connect((host, port))
        print("port {} is listening ".format(port))
        sock.close()
        sock = socket.socket()
    except Exception as exc:
        pass



