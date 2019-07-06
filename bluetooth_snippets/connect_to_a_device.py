# simple inquiry example
import bluetooth

device_to_connect_to = 'nikola'

nearby_devices = bluetooth.discover_devices(duration=5, lookup_names=True)
print("found %d devices" % len(nearby_devices))
devices_bluetooth_addr_map = {}

for addr, name in nearby_devices:
    #print("  %s - %s" % (addr, name))
    devices_bluetooth_addr_map[name] = addr

print(devices_bluetooth_addr_map)

if not devices_bluetooth_addr_map.keys().__contains__(device_to_connect_to):
    print(device_to_connect_to + ' is either not around or its bluetooth is not turned on')
    exit()

socket = bluetooth.BluetoothSocket(bluetooth.AUDIO_SINK_CLASS)
print('Address is ' + (devices_bluetooth_addr_map[device_to_connect_to]))
#something has to added in /etc/blutooth/main.conf
socket.connect((devices_bluetooth_addr_map[device_to_connect_to], 3))
print(socket.recv(1024))
print('connected')
