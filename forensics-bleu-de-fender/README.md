# bleu de fender

by k3ng

---

## Flag

```
COMPFEST16{1mAg3_4S_4ppL1cAt10N_l4YeR_b678cc834b}
```

## Description
bang bang aku mau soal DFIR dong bang

attachment: https://drive.google.com/file/d/1KKMt-I6f4AUv387xKx-EkL_DQfHNvQKe/view?usp=sharing
attachment password: 35f949cd096cf6980750351b80c2c849

## Difficulty
Tingkat kesulitan soal: medium

## Hints
* hint 1
* hint 2
* hint dst.

## Tags
Tags dari soal pisahkan koma (e.g: tags1, tags2, tags3)

## Deployment
Penjelasan cara menjalankan service yang dibutuhkan serta requirementsnya.

#### Contoh 1
- Install docker engine>=19.03.12 and docker-compose>=1.26.2.
- Run the container using:
    ```
    docker-compose up --build --detach
    ```

#### Contoh 2
- How to compile:
    ```
    gcc soal.c -o soal -O2 -D\_FORTIFY\_SOURCE=2 -fstack-protector-all -Wl,-z,now,-z,relro -Wall -no-pie
    ```
- Jalankan:
    ```
    ./soal
    ```
- Workdir di `/home/compfest14`
- Gunakan libc 2.31 ketika sudah keluar. Alias Ubuntu 20.04.

## Notes
Tambahan informasi untuk soal, deployment, atau serangan yang mungkin terjadi pada service soal