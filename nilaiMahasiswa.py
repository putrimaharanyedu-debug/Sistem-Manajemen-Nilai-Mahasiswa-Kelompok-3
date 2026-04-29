class Mahasiswa:
    def __init__(self, nama, nim):
        self.__nama = nama
        self.__nim = nim
        self.__nilai_tugas = 0
        self.__nilai_uts = 0
        self.__nilai_uas = 0
        self.__nilai_akhir = 0

    def __validasi_nilai(self, nilai):
        return 0 <= nilai <= 100

    def set_nilai(self, tugas, uts, uas):
        if all(
            self.__validasi_nilai(n)
            for n in [tugas, uts, uas]
        ):
            self.__nilai_tugas = tugas
            self.__nilai_uts = uts
            self.__nilai_uas = uas
            self.hitung_nilai_akhir()
        else:
            print("Error: Nilai harus 0 - 100")

    def hitung_nilai_akhir(self):
        self.__nilai_akhir = ( 
            self.__nilai_tugas * 0.3
            + self.__nilai_uts * 0.3
            + self.__nilai_uas * 0.4
        )

    def get_nilai_akhir(self):
        return self.__nilai_akhir

    def get_grade(self):
        if self.__nilai_akhir >= 85:
            return "A"
        elif self.__nilai_akhir >= 70:
            return "B"
        elif self.__nilai_akhir >= 60:
            return "C"
        else:
            return "D"

    def update_nilai(self, jenis, nilai_baru):
        if not self.__validasi_nilai(nilai_baru):
            print("Nilai tidak valid")
            return

        jenis = jenis.lower()

        if jenis == "tugas":
            self.__nilai_tugas = nilai_baru
        elif jenis == "uts":
            self.__nilai_uts = nilai_baru
        elif jenis == "uas":
            self.__nilai_uas = nilai_baru
        else:
            print("Jenis nilai tidak dikenal")
            return

        self.hitung_nilai_akhir()
        print("Nilai berhasil diupdate")


    def is_lulus(self):
        if self.__nilai_akhir >= 60:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    def info(self):
        print("NIM   :", self.__nim)
        print("Nama  :", self.__nama)
        print("Tugas :", self.__nilai_tugas)
        print("UTS   :", self.__nilai_uts)
        print("UAS   :", self.__nilai_uas)
        print("Akhir :", round(self.__nilai_akhir, 2))
        print("Grade :", self.get_grade())
        print("Status:", self.is_lulus())
        print("-" * 30)