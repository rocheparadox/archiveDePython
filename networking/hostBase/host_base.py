import http.server
import socketserver
import sys
import os
import argparse



port = 8000  #set 8000 as default serving port
os.chdir(os.getcwd())
parser = argparse.ArgumentParser()
parser.add_argument('--port', '-p', type=int)
parser.add_argument('--dir', '-d', type=str)
args = vars(parser.parse_args())

if args['port'] != None:
    port = args['port'] #Get the port from arguments

if args['dir'] != None:
    dir = args['dir'] #Get the directory to serve from arguments
    os.chdir(dir)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",port), handler)
print("serving",os.getcwd(), "at port :", port,)

try:
    httpd.serve_forever()

except KeyboardInterrupt as exception:
    print('closing server..')
    httpd.server_close()