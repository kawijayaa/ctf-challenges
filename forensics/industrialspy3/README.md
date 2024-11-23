# industrialspy 3

by k3ng

---

## Flag

```
COMPFEST16{t00_3z_3vEN_f0R_4N_1ntErn_abdfe98ce2}
```

## Description
Dear X,

I welcome you to the internship program at Collective Inc. Your first task is to figure out what happened to one of our servers. We have a suspicion that someone logged in and did something. We recovered some files to help you figure this out.

If you have figured it out, submit your report to `nc IP PORT`.

## Difficulty
Tingkat kesulitan soal: easy

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
