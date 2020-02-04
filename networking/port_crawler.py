#Author : Roche Christopher
#File created on 29 Jan 2020 4:04 PM

import socket
import sys, os
import threading

def is_host_alive(hostname):

    response = os.system("ping -c 1 " + hostname)

    # and then check the response...
    if response == 0:
        return True
    else:
        return False

def crawl_ports(start, end):
    sock = socket.socket()
    for port in range(start, end):

        # sys.stdout.write("Checking port {} \r".format(port))
        # sys.stdout.flush()

        try:
            sock.connect((host, port))
            print("port {} is listening ".format(port))
            sock.close()
            sock = socket.socket()
        except Exception as exc:
            pass


if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = input("Enter the host name or IP address:")

if not is_host_alive(host):
    print("Host is not pingable")
    exit()


port_crawler_threads = []

for i in range(0,12):
    start = (i * 5000) + 1
    end = start + 5000
    #print(start)
    port_crawler_thread_temp = threading.Thread( target=crawl_ports, args=(start, end))
    port_crawler_threads.append(port_crawler_thread_temp)

port_crawler_thread_temp = threading.Thread( target=crawl_ports, args=(60000, 65535))
port_crawler_threads.append(port_crawler_thread_temp)

for port_crawler_thread in port_crawler_threads:
    port_crawler_thread.start()



