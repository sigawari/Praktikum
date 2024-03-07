class Mahasiswa:

    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        """
        Args:
          nim (str): Nomor Induk Mahasiswa.
          nama (str): Nama lengkap mahasiswa.
          angkatan (int): Tahun angkatan mahasiswa.
          isMahasiswa (bool): Menandakan apakah objek ini merupakan mahasiswa atau bukan. Default is True.
        """
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    # Setter dan getter untuk nim
    def get_nim(self):
        """Getter untuk NIM."""
        return self.__nim

    def set_nim(self, new_nim):
        """Setter untuk NIM."""
        if not isinstance(new_nim, str):
            raise TypeError("NIM harus berupa string.")
        self.__nim = new_nim

    # Setter dan getter untuk nama
    def get_nama(self):
        """Getter untuk nama."""
        return self.__nama

    def set_nama(self, new_nama):
        """Setter untuk nama."""
        self.__nama = new_nama

    # Method untuk mengecek status aktif (berdasarkan angkatan)
    def cek_status_aktif(self):
        """Mengecek status aktif berdasarkan angkatan."""
        # Asumsikan mahasiswa aktif maksimal 8 semester (4 tahun)
        if self.angkatan >= 2018 and self.angkatan <= 2023:
            return "Aktif"
        else:
            return "Tidak Aktif"

    # Method untuk mengecek status mahasiswa
    def cek_status_mahasiswa(self):
        """Mengecek status mahasiswa berdasarkan status aktif."""
        if self.cek_status_aktif() == "Aktif" and self.isMahasiswa:
            return "Merupakan mahasiswa"
        else:
            return "Bukan mahasiswa"

    # Method untuk mengecek jurusan
    def cek_jurusan(self):
        """Mengecek jurusan berdasarkan NIM.
        """
        nim = self.get_nim()
        if nim[3] == "1" and nim[4] == "4":
            return "Merupakan mahasiswa Informatika"
        else:
            return "Bukan mahasiswa Informatika"


# Input data
nama_mahasiswa = []
nim_mahasiswa = []
angkatan_mahasiswa = []

for i in range(3):
    nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
    nim = input(f"Masukkan NIM mahasiswa ke-{i+1}: ")
    angkatan = int(input(f"Masukkan angkatan mahasiswa ke-{i+1}: "))
    print("\n")

    nama_mahasiswa.append(nama)
    nim_mahasiswa.append(nim)
    angkatan_mahasiswa.append(angkatan)

# Inisiasi object
mahasiswa = []

# Inisiasi objek pertama dengan isMahasiswa = True
mahasiswa.append(Mahasiswa(nim_mahasiswa[0], nama_mahasiswa[0], angkatan_mahasiswa[0]))

# Inisiasi objek kedua tanpa parameter isMahasiswa
mahasiswa.append(Mahasiswa(nim_mahasiswa[1], nama_mahasiswa[1], angkatan_mahasiswa[1]))

# Inisiasi objek ketiga dengan isMahasiswa = False
mahasiswa.append(Mahasiswa(nim_mahasiswa[2], nama_mahasiswa[2], angkatan_mahasiswa[2]))

# Menampilkan informasi
for i in range(3):
    print(f"\nMahasiswa ke-{i+1}")
    print(f"Nama: {mahasiswa[i].get_nama()}")
    print(f"NIM: {mahasiswa[i].get_nim()}")
    print(f"Angkatan: {mahasiswa[i].angkatan}")
    print(f"Status Aktif: {mahasiswa[i].cek_status_aktif()}")
    if i == 1:  # Menampilkan pesan khusus untuk objek kedua
        print("Tidak ada identifikasi untuk data ke-2")
    else:
        print(f"Status Mahasiswa: {mahasiswa[i].cek_status_mahasiswa()}")
    print(f"Jurusan: {mahasiswa[i].cek_jurusan()}")

# Meminta input untuk data yang ingin diubah
index_ubah = int(input("Masukkan nomor mahasiswa yang ingin diubah: ")) - 1

# Meminta nama dan NIM baru
nama_baru = input("Masukkan nama baru: ")
nim_baru = input("Masukkan NIM baru: ")

# Mengubah data
mahasiswa[index_ubah].set_nama(nama_baru)
mahasiswa[index_ubah].set_nim(nim_baru)

# Menampilkan informasi setelah perubahan
print("\nData mahasiswa setelah diubah:")
print(f"Nama: {mahasiswa[index_ubah].get_nama()}")
print(f"NIM: {mahasiswa[index_ubah].get_nim()}")

# Menampilkan informasi seluruh mahasiswa setelah perubahan
print("\nData seluruh mahasiswa setelah perubahan:")
for i in range(3):
    print(f"\nMahasiswa ke-{i+1}")
    print(f"Nama: {mahasiswa[i].get_nama()}")
    print(f"NIM: {mahasiswa[i].get_nim()}")
    print(f"Angkatan: {mahasiswa[i].angkatan}")
    print(f"Status Aktif: {mahasiswa[i].cek_status_aktif()}")
    print(f"Status Mahasiswa: {mahasiswa[i].cek_status_mahasiswa()}")
    print(f"Jurusan: {mahasiswa[i].cek_jurusan()}")