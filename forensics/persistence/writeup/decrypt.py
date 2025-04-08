import re
from pyshark import FileCapture
from base64 import b64decode
from Crypto.Cipher import ARC4

packets = FileCapture("./network.pcapng", display_filter="http &&  _ws.col contains \"employees\"")

data = b""

for packet in packets:
    b64 = packet.HTTP.authorization.split()[-1].split(".")[-1]
    decoded = b64decode(b64 + "==")
    decrypted = ARC4.new(b"hello!").decrypt(decoded)
    data += decrypted

data = data[data.find(b"[SHIFT]RECURSIO"):]
flag = []
i = 0
shift = False

while i < len(data):
    if data[i:].startswith(b"["):
        if data[i+1:].startswith(b"SHIFT"):
            shift = not shift
            i += 6
        elif data[i+1:].startswith(b"Back"):
            flag = flag[:-1]
            i += 5
    else:
        if shift:
            flag.append(chr(data[i]))
        else:
            flag.append(chr(data[i]).lower())

    i+=1

print("".join(flag))
