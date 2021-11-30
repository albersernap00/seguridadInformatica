#!/usr/bin/python3

from scapy.all import *

counter = 0
packets = []

def print_pkt(capture):
    global counter
    counter += 1
    packets.append(capture)
    print ("Paquete " + str(counter) + ": " + capture[0][1].src + " => " + capture[0][1].dst)

capture = sniff(filter="icmp", prn=print_pkt)
wrpcap("temp.cap", packets)
capture.summary()