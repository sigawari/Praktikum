'''
Buatlah sebuah program Python menghitung luas dan keliling lingkaran yang meminta
pengguna untuk memasukkan jari-jari lingkaran. Setelah itu, program harus menghitung dan
mencetak luas serta keliling lingkaran tersebut. Pastikan program dapat menangani input

yang tidak valid (misalnya, jika pengguna memasukkan nilai negative mengoutputkan “jari-
jari lingkarang tidak boleh negatif”). Dengan rumus keliling lingkaran dan luas
2 pi r dan pi r^2
lingkaran
pi = 3.14 '''

pi = 3.14

while True:
    jari = int(input("Masukkan jari-jari lingkaran: "))

    if jari >=0:
        break
    else:
        print("Jari-jari lingkaran tidak boleh negatif")

luas = pi * jari * jari
keliling = 2 * pi * jari

print ("\n========================================")
print ("Luas Lingkaran : ", luas)
print ("Keliling Lingkaran : ", keliling)
print ("========================================\n")


print ("-Thanks for using the program ^^")