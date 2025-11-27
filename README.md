# **LAPORAN PRAKTIKUM 6**

## **Pengantar Pemrograman – Lab 6**

### **Sub Rutin / Fungsi**

**Nama** : Naziha Raiqi Aribino<br>
**Kelas** : TI.25.A2<br>
**NIM** : 312510232<br>
**Mata Kuliah** : Pengantar Pemrograman<br>
**Praktikum** : Lab 6 — Sub Rutin / Fungsi<br>

---

# **1. Tujuan Praktikum**

1. Memahami konsep dasar fungsi pada Python.
2. Mampu membuat fungsi dengan parameter dan return value.
3. Mampu menggunakan default argument, keyword argument, dan `*args`.
4. Mengubah fungsi biasa menjadi lambda function.
5. Membuat aplikasi sederhana menggunakan fungsi untuk mengelola data mahasiswa.

---

# **2. Dasar Teori**

## **2.1 Fungsi**

Fungsi adalah blok kode yang digunakan untuk menjalankan tugas tertentu. Fungsi membantu membuat program lebih modular, rapi, dan mudah dipelihara.

Contoh:

```python
def halo():
    print("Hello dunia!")
```

## **2.2 Parameter dan Return Value**

Parameter digunakan untuk menerima input, sedangkan `return` mengembalikan nilai.

```python
def jumlah(a, b):
    return a + b
```

## **2.3 Default Argument**

Parameter yang sudah memiliki nilai bawaan.

```python
def salam(nama="User"):
    print("Halo", nama)
```

## **2.4 Arbitrary Arguments (*args)**

Memungkinkan pengiriman jumlah parameter yang tidak terbatas.

```python
def total(*angka):
    return sum(angka)
```

## **2.5 Lambda Function**

Fungsi anonim (tanpa nama) yang ditulis 1 baris.

```python
tambah = lambda x, y: x + y
```

---

# **3. Praktikum**

---

# **3.1 LATIHAN 1 — Mengubah Fungsi Menjadi Lambda**

### **Kode Program:**

```python
import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))

print("Hasil a(5):", a(5))
print("Hasil b(3, 4):", b(3, 4))
print("Hasil c(2, 4, 6, 8):", c(2, 4, 6, 8))
print("Hasil d('hello'):", d("hello"))
```

### **Output Program:**

```
Hasil a(5): 25
Hasil b(3, 4): 5.0
Hasil c(2, 4, 6, 8): 5.0
Hasil d('hello'): hlo   (urutan bisa berubah karena set)
```

---

# **3.2 TUGAS PRAKTIKUM — Program Data Nilai Mahasiswa**

### **Kode Program:**

```python
data_mahasiswa = {}

def tambah():
    print("\n=== Tambah Data Mahasiswa ===")
    nama = input("Masukkan Nama: ")
    nilai = float(input("Masukkan Nilai: "))
    data_mahasiswa[nama] = nilai
    print(f"Data '{nama}' berhasil ditambahkan!")

def tampilkan():
    print("\n=== Daftar Nilai Mahasiswa ===")
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        for nama, nilai in data_mahasiswa.items():
            print(f"- {nama}: {nilai}")

def hapus(nama):
    print("\n=== Hapus Data Mahasiswa ===")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data '{nama}' berhasil dihapus!")
    else:
        print(f"Data '{nama}' tidak ditemukan!")

def ubah(nama):
    print("\n=== Ubah Data Mahasiswa ===")
    if nama in data_mahasiswa:
        nilai_baru = float(input("Masukkan nilai baru: "))
        data_mahasiswa[nama] = nilai_baru
        print(f"Data '{nama}' berhasil diubah!")
    else:
        print(f"Data '{nama}' tidak ditemukan!")

while True:
    print("\n===============================")
    print("      PROGRAM DATA NILAI")
    print("===============================")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Nama yang ingin dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Nama yang ingin diubah: ")
        ubah(nama)
    elif pilihan == "5":
        print("\nProgram selesai. Terima kasih!\n")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")
```

---

# **4. Flowchart Program (Teks)**

```
          +-------------------+
          |       MULAI       |
          +---------+---------+
                    |
                    v
          +-------------------+
          | Tampilkan Menu    |
          +---------+---------+
                    |
                    v
          +-------------------+
          | Pilihan User?     |
          +--+----+-----+----+
             |    |     |    |
             v    v     v    v
           Tambah Lihat Hapus Ubah
             |    |     |    |
             v    v     v    v
       Proses Tambah/Lihat/Hapus/Ubah
                    |
                    v
          +-------------------+
          |   Pilih Lagi?     |
          +--------+----------+
                   |
                  (5) Keluar
                   |
                   v
          +-------------------+
          |      SELESAI      |
          +-------------------+
```

---

# **5. Kesimpulan**

1. Penggunaan fungsi membuat program lebih terstruktur dan mudah dikelola.
2. Lambda function dapat digunakan untuk membuat fungsi sederhana secara ringkas.
3. Melalui praktikum ini, mahasiswa dapat membuat program CRUD sederhana dengan fungsi.
4. Program dapat menambah, menampilkan, menghapus, dan mengubah data mahasiswa dengan baik.

---

# **6. Dokumentasi**

Program telah diuji pada Python dan berjalan tanpa error.

**Laporan Praktikum Selesai**
