# industrialspy 2

by k3ng

---

## Flag

```
NETSOS{y0U_jU5t_g0t_K3y_L0gGeD_h3h3}
```

## Description
After we intercepted Lyubov's last attempt at stealing documents, she disabled our RAM capturer. Fortunately, we still have other loggers active. Is she still trying?

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
