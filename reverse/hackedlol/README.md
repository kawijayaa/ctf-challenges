# hackedlol

by k3ng

---

## Flag

```
COMPFEST15{wH4t_3veN_1s_tH1s_enCryPt10n_LOLZ_ab533e4f00}
```

## Description
Someone hacked my computer! I really need my important file but it's encrypted. The IT guy managed to recover one file. But I don’t think that is my file though.

## Difficulty
easy

## Hints
* hint 1
* hint 2
* hint dst.

## Tags
Python Bytecode, Obfuscation

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
