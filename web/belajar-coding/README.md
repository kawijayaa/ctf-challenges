# belajar coding

by k3ng

---

## Flag

```
NETSOS{p3nyer7a4n_f1l3_l0k4l_h3h3h3_42fbc06b40}
```

## Description
i made a website to help my friend to know about programming languages. it's my first time using php so i hope it's safe.

## Difficulty
Tingkat kesulitan soal: easy

## Hints
* hint 1
* hint 2
* hint dst.

## Tags
web, lfi

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
