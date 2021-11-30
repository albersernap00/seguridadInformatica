#!/usr/bin/python3

from scapy.all import * 

print('Introduce id del paquete ICMP:')
idICMP = input()

while(True):
    a = IP()
    a.dst = '155.210.71.184' #C
    a.src = '155.210.71.165' #A

    b = ICMP()
    b.id = int(idICMP, 16)

    p = a/b

    send(p)
