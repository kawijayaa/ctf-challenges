from scapy.all import *

packets = rdpcap('test.pcapng')

mapping = {
    0x04 : "a", 0x05 : "b", 0x06 : "c", 0x07 : "d", 0x08 : "e", 0x09 : "f", 0x0A : "g", 
    0x0B : "h", 0x0C : "i", 0x0D : "j", 0x0E : "k", 0x0F : "l", 0x10 : "m", 0x11 : "n", 
    0x12 : "o", 0x13 : "p", 0x14 : "q", 0x15 : "r", 0x16 : "s", 0x17 : "t", 0x18 : "u", 
    0x19 : "v", 0x1A : "w", 0x1B : "x", 0x1C : "y", 0x1D : "z", 
    0x1E : "1", 0x1F: "2", 0x20: "3", 0x21: "4", 0x22: "5", 0x23: "6", 0x24: "7", 0x25: "8", 0x26: "9", 0x27: "0", 
    0x28: "\n", 0x2A: "DELETE", 0x2C: " ", 0x2D: "_", 0x2E: "=", 0x2F: "{", 0x30: "}", 0x33: ":", 0x36: ",", 0x37: ".", 0x38: "/"}

res = ""
for packet in packets:
    shift = packet.load[-8] == 0x02
    if len(packet.load) == 35:
        try:
            hx = mapping.get(packet.load[-6]).upper() if shift else mapping.get(packet.load[-6])
            if hx == "DELETE":
                res = res[:-1]
            elif hx == "/" and shift:
                res += "?"
            else:
                res += (hx if hx else "")
        except:
            continue
print(res)
