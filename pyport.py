import socket
import pyfiglet

#ASCII banner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

#Defining the target (input)
target = input("Target IP: ")
print("-" * 50)

# Creating the socket (s) and defining the address family (AF_INET - IPV4) and protocol (SOCK_STREAM - TCP)
# Attempt to connect to the target
def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

# Scan all standardized ports (1-1023)
# Output the results
for port in range(1, 1024):
    result = portscan(port)
    if(result):
        print("Port {} is open!".format(port))
    else:
        print("Port {} is closed...".format(port))
