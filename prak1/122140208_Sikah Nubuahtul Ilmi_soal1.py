'''
Buatlah sebuah program Python untuk menghitung jumlah bilangan ganjil dalam rentang
tertentu.
• Anda diminta untuk membuat sebuah program Python yang menerima dua input
dari pengguna: batas bawah (lower) dan batas atas (upper) dari rentang bilangan.
• Program kemudian harus menghitung dan mencetak jumlah bilangan ganjil di antara
kedua batas tersebut.
• Jika batas atas ataupun batas bawah yang di inputkan nilainya di bawah nol, akan
mengoutputkan “Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol”. '''
print ("========================================")
print ("Program Hitung Banyaknya Bilangan Ganjil")
print ("========================================\n")

bawah = int(input("Batas bawah : "))
atas = int(input("Batas atas : "))
count = 0

for i in range(atas):
    if i >= bawah and i % 2 != 0:
        count+=1
        print(i)

print ("\n========================================")
print ("Total Banykanya Bilangan Ganjil : ", count)
print ("========================================\n")

print ("-Terima kasih telah menggunakan program ^^")