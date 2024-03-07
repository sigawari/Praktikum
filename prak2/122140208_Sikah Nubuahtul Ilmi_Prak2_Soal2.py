class InventarisHumas:
    def __init__(self):
        self.stok = {
            'kamera': 10,
            'stabilizer': 5,
            'mikrofon': 15,
            'komputer': 20,
            'keyboard': 30
        }

    # Mengurangi stok barang jika barang tersedia
    def kurangi_stok(self, item, jumlah):
        if item in self.stok and self.stok[item] >= jumlah:
            self.stok[item] -= jumlah
            print(f"{jumlah} {item}(s) telah diambil dari inventaris.")
        else:
            print(f"Maaf, stok {item} tidak mencukupi.")

    # Menambahkan stok barang
    def tambahkan_stok(self, item, jumlah):
        if item in self.stok:
            self.stok[item] += jumlah
            print(f"{jumlah} {item}(s) telah ditambahkan ke inventaris.")
        else:
            print(f"Barang {item} tidak ditemukan dalam inventaris.")

    # Menampilkan stok barang
    def tampilkan_inventaris(self):
        print("Inventaris Saat Ini:")
        for item, jumlah in self.stok.items():
            print(f"{item.capitalize()}: {jumlah}")


# Fungsi untuk memproses input
def main():
    inventaris_humas = InventarisHumas()
    print("==SELAMAT DATANG DI STUDIO HUMAS ITERA==")
    
    while True:
        print("Menu:")
        print("1. Tampilkan Inventaris")
        print("2. Kurangi Stok")
        print("3. Tambahkan Stok")
        print("4. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            inventaris_humas.tampilkan_inventaris()
        elif pilihan == '2':
            item = input("Masukkan barang yang ingin dikurangi stoknya: ").lower()
            jumlah = int(input("Masukkan jumlah barang yang ingin dikurangi: "))
            inventaris_humas.kurangi_stok(item, jumlah)
        elif pilihan == '3':
            item = input("Masukkan barang yang ingin ditambahkan stoknya: ").lower()
            jumlah = int(input("Masukkan jumlah barang yang ingin ditambahkan: "))
            inventaris_humas.tambahkan_stok(item, jumlah)
        elif pilihan == '4':
            print("Terima kasih telah main ke Humas! Sampai jumpa.")
            break
        else:
            print("Maaf, pilihan tidak valid. Silakan coba lagi.")


# Menjalankan program
if __name__ == "__main__":
    main()
