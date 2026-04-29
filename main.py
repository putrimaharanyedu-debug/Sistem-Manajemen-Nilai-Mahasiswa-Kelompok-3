from nilaiMahasiswa import Mahasiswa

def main():
    daftar_mahasiswa = []

    while True:
        print("\nSISTEM MANAJEMEN NILAI")
        print("1. Tambah Mahasiswa & Nilai")
        print("2. Tampilkan Data")
        print("3. Update Nilai")
        print("4. Urutkan Nilai Tertinggi")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama : ")
            nim = input("NIM  : ")

            mhs = Mahasiswa(nama, nim)

            try:
                tugas = float(input("Nilai Tugas : "))
                uts = float(input("Nilai UTS   : "))
                uas = float(input("Nilai UAS   : "))

                mhs.set_nilai(tugas, uts, uas)
                daftar_mahasiswa.append(mhs)

            except ValueError:
                print("Input harus angka")

        elif pilihan == "2":
            for mhs in daftar_mahasiswa:
                mhs.info()

        elif pilihan == "3":
            nim = input("Masukkan NIM: ")

            target = next(
                (
                    m for m in daftar_mahasiswa
                    if m.get_nim() == nim
                ),
                None
            )

            if target:
                jenis = input("Jenis nilai: ")
                nilai = float(input("Nilai baru : "))
                target.update_nilai(jenis, nilai)
            else:
                print("Mahasiswa tidak ditemukan")

        elif pilihan == "4":
            daftar_mahasiswa.sort(
                key=lambda x: x.get_nilai_akhir(),
                reverse=True
            )

            print("Data berhasil diurutkan")

            for mhs in daftar_mahasiswa:
                mhs.info()

        elif pilihan == "5":
            print("Terimakasih telah menggunakan sistem ini.")
            break

        else:
            print("Pilihan tidak tersedia")


if __name__ == "__main__":
    main()
    
    
    
# Bagian Output