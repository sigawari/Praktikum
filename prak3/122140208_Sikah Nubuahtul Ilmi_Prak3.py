'''
Buatlah sebuah kelas Dagangan yang memiliki atribut instance berupa nama, 
stok, dan harga (bersifat private) yang nilainya tidak sama untuk tiap instansinya. 
Selain itu, kelas Dagangan tersebut juga memiliki atribut kelas berupa 
jumlah_barang dan list_barang (berisi data-data nama, stok, dan harga barang tiap 
instansi) yang konsisten pada tiap instansi Dagangan yang telah dibuat. Gunakan 
fungsi bantuan yaitu lihat_barang() untuk menampilkan output dari jumlah_barang 
dan list_barang.
Contoh main program (kalian cukup buat kode untuk class Dagangan):
Dagangan1 = Dagangan(“Galon Aqua 19L”, 32, 17000)
Dagangan2 = Dagangan(“Gas LPG 5 kg”, 22, 88000)
Dagangan3 = Dagangan(“Beras Ramos 5 kg”, 13, 68000)
Dagangan.lihat_barang()
del Dagangan1
Dagangan.lihat_barang()
Output program tersebut (tiap instansi akan memberikan nilai konsisten satu sama 
lain):
Jumlah barang dagangan pada toko: 3 buah
1. Galon Aqua 19L seharga Rp 17000 (stok: 32)
2. Gas LPG 5 kg seharga Rp 88000 (stok: 22)
3. Beras Ramos 5 kg seharga Rp 68000 (stok: 13)
Galon Aqua 19L dihapus dari toko!
Jumlah barang dagangan pada toko: 2 buah
1. Gas LPG 5 kg seharga Rp 88000 (stok: 22)
2. Beras Ramos 5 kg seharga Rp 68000 (stok: 13)
Gas LPG 5 kg dihapus dari toko!
Beras Ramos 5 kg dihapus dari toko
'''
class Dagangan:
  def __init__(self, nama, stok, harga):
    # Atribut instance
    self._nama = nama
    self._stok = stok
    self._harga = harga

    # Menambahkan data ke atribut kelas
    Dagangan.jumlah_barang += 1
    Dagangan.list_barang.append((self._nama, self._stok, self._harga))

  # Atribut 
  jumlah_barang = 0
  list_barang = []

  def lihat_barang(self):
    print("\n===================================")
    print(f"Jumlah barang dagangan pada toko: {Dagangan.jumlah_barang} buah")
    for i in range(Dagangan.jumlah_barang):
      print(f"{i + 1}. {Dagangan.list_barang[i][0]} seharga Rp {Dagangan.list_barang[i][2]} (stok: {Dagangan.list_barang[i][1]})")

  def __del__(self):
    print(f"\n{self._nama} dihapus dari toko!")
    Dagangan.jumlah_barang -= 1
    Dagangan.list_barang.remove((self._nama, self._stok, self._harga))

# Main program berdasarkan soal
Dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan1.lihat_barang()

del Dagangan1

Dagangan2.lihat_barang()

del Dagangan2

del Dagangan3 #Menyesuaikan output dari soal yang dibagikan