import daemon
import time
import os

#print(os.getpid())
daemon.basic_daemonize()

while True:
    with open("daemonize_check.txt","a") as test_file:
        test_file.write(str(time.time()) + "\n")
        time.sleep(2)
