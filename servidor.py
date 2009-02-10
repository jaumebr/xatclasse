#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
dgramSock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
dgramSock.bind( ('', 8080) )
dgramSock.listen(10)
msg2 = ""
while (msg2 <> "quit!"):
  (addr, port) = dgramSock.accept()
#dgramSock.recvfrom( 100 )
  #dgramSock.sendto( msg, (addr, port) )
  #msg = addr.recv(100)
  msg = addr.recv(300)
  print msg
  addr.close()
  msg2 = msg[0:5]
  #print msg2
dgramSock.close()
