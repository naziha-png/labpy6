# Program Daftar Nilai Mahasiswa
# Tugas Praktikum - Lab 6
# Fungsi: tambah(), tampilkan(), hapus(nama), ubah(nama)
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
# ==== Program Utama (Menu) ====
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
