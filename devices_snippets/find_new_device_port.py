#This snippet is used to find the port to which the newly connected device is assigned to..
import os
pre_connected_devices=os.listdir('/dev')
input("Connect the device and press enter..")
post_connected_devices=os.listdir('/dev')
connected=False

for dev in post_connected_devices:
    if dev not in pre_connected_devices:
        print(dev)
        connected=True
        break

if not connected:
    print("No new devices were connected..")


