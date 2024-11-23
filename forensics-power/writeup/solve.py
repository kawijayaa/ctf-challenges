from Crypto.Cipher import AES
import pyshark
import base64
import re
import binascii

packets = pyshark.FileCapture("../public/capture.pcapng")
flag = ""

for packet in packets:
    if 'HTTP' in packet and packet.tcp.dstport == '6969':
        payload = packet.http.request_uri_query[6:]
        payload = base64.b64decode(payload).decode()
        print(payload)
        strings = re.findall("\"(.+?)\"", payload)

        payload = strings[0]
        key = strings[1]

        cipher = AES.new(binascii.unhexlify(key), AES.MODE_CBC, binascii.unhexlify(key))
        char = cipher.decrypt(base64.b64decode(payload))
        flag += char.decode()[0]

print(flag)
