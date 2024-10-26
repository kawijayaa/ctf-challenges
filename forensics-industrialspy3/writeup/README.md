# Writeup industrialspy 3

1. Traffic diawal adalah traffic nmap. Bisa dicheck port yang open dengan filter wireshark `tcp.flags == 0x010`
2. Filter `pgsql` dan cari paling bawah ada username dan passwordnya.
3. Cari packet dimana user execute `SELECT * FROM employees WHERE username = 'super'` dan crack SHA1 hashnya pake wordlist rockyou.
4. Cari packet dimana user execute `DELETE FROM penalties WHERE ...`
5. Cari nama dari packet dimana user execute `SELECT * FROM emplyoees` dan cari employee ID yang digunakan di nomor 4.
