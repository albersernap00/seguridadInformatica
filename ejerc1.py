#!/usr/bin/python3

from scapy.all import * 

def print_pkt(pkt):
    pkt.show()

pkt = sniff(prn=print_pkt)
pkt.summary()



