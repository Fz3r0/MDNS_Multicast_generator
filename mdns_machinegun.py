from scapy.all import *
import re
import string

target_ip = sys.argv[1]

# mdns query string
query = "_services._dns-sd._udp.local"

# build and send the packet
pkt=IP(dst=192.168.1.100)/UDP(dport=5353)/DNS(rd=1,qd=DNSQR(qname=query,qtype='PTR'))
ans=sr1(pkt,verbose=0,timeout=2)
