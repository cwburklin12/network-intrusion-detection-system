# Network Intrusion Detection System
from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def main():
    print("Starting Network Intrusion Detection System...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()