#!/usr/bin/python3

from scapy.all import * 

a = IP()
a.dst = '155.210.71.165'
a.src = '155.210.71.1'

b = ICMP()

p = a/b

send(p)
