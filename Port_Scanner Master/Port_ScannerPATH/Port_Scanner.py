#!/usr/bin/env python3
#Port_Scanner.py
#THIS IS TO BE USED FOR EDUCATIONAL PURPOSES ONLY
#JTH or Vesuvian Hector are not responsible for any misuse of this tool.


#Modules
import os
import socket
import subprocess
import sys
from colored import fg, bg, attr
from datetime import datetime


#Banner&Color
Banner = fg('#00FF00') + bg('#808080') + attr(5)
color  = fg('#FF0000') + bg('#808080')
reset = attr(25)

#BANNER
print (Banner)
banner = '/home/vesuvian/Port_Scanner/Port_Scanner Banner.txt'
f  = open(banner,"r")
ascii = "".join(f.readlines())
print(Banner + ascii)
print("BY:JTH & Vesuvian Hector")
print (reset)

# Ask for input
print(color)
print("_"*60)
print ("Please provide the following information")
remoteServer    = input("Enter a target to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
Low_port  = input("Enter lowest port:" )
High_port = input("Enter highest port:" )

    
print ("-" * 60)
print ("Please wait, scanning target", remoteServerIP)
print ("-" * 60)

# Check what time the scan started
time1 = datetime.now()
print (time1)

#Port Scanner Chunk
try:
    
    for port in range(int(Low_port),int(High_port)):  #65535
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        r = s.connect_ex((remoteServerIP, port))
        if r == 0:
            print ("Port {}: 	 Open".format(port))
    
        else:
            print ("Port {}: 	 Closed".format(port))
            
        s.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname of target could not be resolved. restarting')

except socket.error:
    print ("Couldn't connect to target. restarting") 
#__________________________________________________________________________________#

#Timer ends
time2 = datetime.now()

print (time2)                                                   

total =  time2 - time1

print ('Scanning Completed in: ', total)


