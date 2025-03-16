from pyshark import FileCapture
from base64 import b64decode
from binascii import unhexlify
from Crypto.Cipher import AES

packets = FileCapture("../public/collection.pcapng", display_filter="http && ip.dst == 192.168.76.131 && http.request.uri.query")

for packet in packets:
    payload = packet.HTTP.request_uri_query[2:]
    decoded = unhexlify(b64decode(payload).replace(b":", b""))
    aes = AES.new(b64decode("c2RqYWhsZGtzYWprZGx3YQ=="), mode=AES.MODE_ECB)
    decrypted = aes.decrypt(decoded).decode().strip().split("johndoe ")[-1]
    print(decrypted)
