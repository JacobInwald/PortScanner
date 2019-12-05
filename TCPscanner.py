import socket
import subprocess
import sys
from datetime import datetime


socket.setdefaulttimeout(1)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

# remove extraneous items from screen
subprocess.call('clear', shell=True)

# get ye old input from user
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
firstPort = int(input("Enter First Port: "))
lastPort = int(input("Enter Last Port: "))

#prints cool boy banner
print("-" * 60)
print("Host Finder", remoteServerIP)
print("-" * 60)

t1 = datetime.now()
timerStart = datetime.now()

#makes sure if the port isn't right it catches it
try:
    for port in range(firstPort,lastPort):
        print(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #socket.setdefaulttimeout(2)
        #socket.settimeout(1)
        #socket.setblocking(0)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()
#classic interrupt stuff
except KeyboardInterrupt:
    print("Exiting...")
    sys.exit()
#wrong hostname exception
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()
#wrong port exception
except socket.error:
    print("Couldn't connect to server")
    sys.exit()

#second cool boy time check
t2 = datetime.now()

#cool boy runtime
total =  t2 - t1
print('Scanning Completed in: ', total)
