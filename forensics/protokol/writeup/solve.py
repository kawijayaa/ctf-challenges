from scapy.all import *
import zlib
import pickle

packets = rdpcap('./public/capture.pcapng')
res = {}

for packet in packets:
    if packet.haslayer(IP) and packet.getlayer(IP).dst == '69.69.69.69':
        if packet.haslayer(UDP) and packet.haslayer(Raw):
            offset = (packet.getlayer(UDP).dport - 8000) // 10
            payload = packet.getlayer(Raw).load
            decompressed = zlib.decompress(payload)
            res[offset] = decompressed[6:]
            print(decompressed)

for r in sorted(res.keys()):
    pickle.loads(res[r])
