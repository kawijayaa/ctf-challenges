from os.path import isfile
import os
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
from PIL import Image

count = 0
for png in os.listdir("./test/"):
    print(png)
    if isfile("./test/" + png):
        img = Image.open("./test/" + png)
        pixels = img.load()
        bit_string = ""
        
        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = pixels[x,y]
                bit_string += str(r & 1)
                bit_string += str(g & 1)
                bit_string += str(b & 1)

        bin = bytes(int(bit_string[i : i + 8], 2) for i in range(0, len(bit_string), 8))
        decrypted = Blowfish.new(b"adminganteng", Blowfish.MODE_CBC, b"kriptodd").decrypt(pad(bin, Blowfish.block_size))
        with open("./final/" + png, "wb") as f:
            f.write(decrypted)
        count += 1
