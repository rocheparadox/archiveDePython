#This snippet is used to find the port to which the newly connected device is assigned to..

import os
new_device=False
pre_connected_devices=os.listdir('/dev')
input("Connect the device and press enter..")
post_connected_devices=os.listdir('/dev')

for dev in post_connected_devices:
    if dev not in pre_connected_devices:
        print(dev)
        new_device=True
        break

if not new_device:
    print("No new devices were connected...")