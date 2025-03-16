# Writeup collection

Pas request `http://192.168.76.131/search` bakal download script powershell dimana file itu bakal exfiltrate data dari clipboard, di convert jadi hex terus di encrypt pake AES-ECB dan dikirim ke `http://192.168.76.131/search?q=<payload>`
