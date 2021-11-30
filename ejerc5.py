#!/usr/bin/python3

from scapy.all import * 

print('Introduce id del paquete ICMP:')
idICMP = input()

a = IP()
a.dst = '155.210.71.184' #C
a.src = '155.210.71.165' #A

b = ICMP()
b.id = idICMP

ls(b)

p = a/b

send(p)