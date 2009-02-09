#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
dgramSock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
dgramSock.bind( ('', 8080) )
while 1:
  msg, (addr, port) = dgramSock.recvfrom( 100 )
  dgramSock.sendto( msg, (addr, port) )
  print msg
