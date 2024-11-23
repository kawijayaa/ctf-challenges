from binascii import hexlify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
import string
import random
import os
import requests

TEMPLATE = '${0}=[sYsTEm.ConVErT]::FromBase64String("{5}");sTart-sLeEp -SecoNDS 5;${1}=[sYsTEm.ConVErT]::FromHexString("{6}");starT-SlEEP -seCOnDS 5;${2}=New-Object System.Security.Cryptography.AesManaged;StarT-sLeep -seCONds 20;${2}.Key=${1};${2}.IV=${1};sTArt-SleEP -sEcOndS 20;$d=${2}.CreateDecryptor();${4}=[sYsTEm.teXT.enCodING]::UTF8.GetString($d.TransformFinalBlock(${0},0,${0}.Length));'
FLAG = 'NETSOS{gimana_caranya_ya_biar_flag_soal_ini_panjang_biar_pada_scripting_hmmmmmmmmmmmm_ah_aku_tau_flagnya_isi_ngasal_aja_akwowakowakowakawo}'
VARIABLE_LENGTH = 64

def random_string(length):
    return ''.join([random.choice(string.ascii_letters) for _ in range(length)])

def gen_payload(text, key):
    return b64encode(TEMPLATE.format(random_string(VARIABLE_LENGTH), random_string(VARIABLE_LENGTH), random_string(VARIABLE_LENGTH), random_string(VARIABLE_LENGTH), random_string(VARIABLE_LENGTH), text, key).encode()).decode()

def encrypt(text):
    key = os.urandom(16)
    iv = key
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return b64encode(cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))).decode(), hexlify(key).decode(), hexlify(iv).decode()

for c in FLAG:
    encrypted, key, iv = encrypt(c)
    payload = gen_payload(encrypted, key)
    requests.get("http://localhost:6969?search=" + payload)
