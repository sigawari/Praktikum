'''
Buatlah dua kelas Persegi dan Lingkaran dengan metode hitungLuas(). Gunakan konsep
polimorfisme agar kita dapat menghitung luas dari objek berbentuk persegi atau lingkaran
tanpa memeriksa jenis objek secara eksplisit.
Contoh output:
persegi = Persegi(5)
lingkaran = Lingkaran(3)
print(f"Luas Persegi: {persegi.hitungLuas()}") # Output: Luas Persegi: 25
print(f"Luas Lingkaran: {lingkaran.hitungLuas()}") # Output: Luas Lingkaran:
28.274333882308138
'''
import math #memanggil math bawaan python

class BangunDatar: #class abstrak untuk pendefinisian
    def __init__(self, sisi, jari):
        self.sisi = sisi
        self.jari = jari

    def hitungLuas(self):
        pass

class Persegi(BangunDatar):
    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(BangunDatar):
    def hitungLuas(self):
        return math.pi * self.jari ** 2

persegi = Persegi(5, None)  # Persegi memiliki sisi, tapi tidak memerlukan jari-jari
lingkaran = Lingkaran(None, 3)  # Lingkaran memiliki jari-jari, tapi tidak memerlukan sisi

for bangundat in (persegi, lingkaran):  # Menggunakan objek yang sudah dibuat
    print(f"Luas: {bangundat.hitungLuas()}")  # Memanggil metode hitungLuas() 
