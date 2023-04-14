import scapy.all as scapy


def scan(ip):
    arprequest= scapy.ARP(pdst=ip)
    print(arprequest.summary())
	
	
scan("192.168.1.1/24")
