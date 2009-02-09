#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import socket
dgramSock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
dgramSock.sendto( "Hello World\n", ('', 8080) )
print dgramSock.recv( 100 )
dgramSock.close()

