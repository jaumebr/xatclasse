#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import socket

def enviarMissatge(linia):
  dgramSock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
  dgramSock.connect(("127.0.0.1",8080))
  dgramSock.sendto( linia + "\n", ('', 8080) )
  dgramSock.close()

lin = ""
while (lin <> "quit!"):
  lin = raw_input("Enviar missatge: ")
  enviarMissatge(lin)

#enviarMissatge("quit!")