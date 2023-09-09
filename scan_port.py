#!/usr/python3

from datetime import datetime 
import sys
import socket

# define target
if len(sys.argv)==2:
    target =socket.gethostbyname (sys.argv[1])#translate host name to IPv4

else:
    print ("invalid arguments")
    print ("syntax: python3 scan_port.py")
    sys.exit()

print("-"*60)
print ("scanning target" +target)
print ("time started:"+str(datetime.now()))
print ("-" *60)

try:
    for port in range(1,254):
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #return error indicator
        print("checking port{}".format(port))
        if result ==0:
            print ("port{} is open".format (port))      
        s.close()

except KeyboardInterrupt:
    print ("\n exiting program")
    sys.exit()

except socket.gaierror:
    print ("host name is not resolved")
    sys.exit()

except socket.error:
    print ("counldn't connect to server")
    sys.exit()
