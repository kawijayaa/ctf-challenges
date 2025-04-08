Part 1:

Command yang menarik yang digunakan attacker adalah `docker run` dimana sebuah container dengan image bernama `k3ngg/c2` di run di machine victim. Image tersebut di host di Docker Hub, jadi imagenya bisa dilakukan analisis. Ada salah satu file `/bin/pydoc` yang diremove saat build docker image. File itu isinya flag part 1

Part 2:

Dari executable python `/bin/socat`, terlihat ada C2 yang hasilnya akan diexfiltrate ke sebuah repository GitHub dengan enkripsi RC4. Karena PAT tokennya disimpan di image docker, repositorynya bisa dipull dan di decrypt isinya. Salah satu dari hasil C2 nya adalah flag part 2.

Ada unintended dimana flag part 2 bisa diambil dari salah satu packet TCP ketika attacker mengirimkan command untuk print flag part 2 tersebut.

Part 3:

Salah satu hasil exfiltration dari C2 adalah sebuah file yang memberikan password dari victim (`16john`). Password tersebut bisa digunakan untuk decrypt traffic SMB untuk mendapatkan flag part 3
