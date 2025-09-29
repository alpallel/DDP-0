jumlah_persegi = int(input("Jumlah persegi: "))
panjang_sisi = int(input("Panjang sisi: "))

print("* " * (panjang_sisi - 1) * jumlah_persegi + "*")
for i in range(jumlah_persegi):
    for j in range(1, panjang_sisi):
        if j == panjang_sisi - 1:
            print("* " * (panjang_sisi - 1) * jumlah_persegi + "*")
        else:
            print(("* " + "  " * (panjang_sisi - 2)) * (jumlah_persegi + 1))