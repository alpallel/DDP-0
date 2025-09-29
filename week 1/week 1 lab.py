sisi = int(input("Panjang sisi: "))
n = int(input("Jumlah persegi: "))
a = 0

for i in range(n):
    if i == 0:
        a = 0
    else:
        a = 1
    for j in range(a, sisi):
        for k in range(n):
            if k == 0:
                a = 0
            else:
                a = 1
            for l in range(a, sisi):
                if j == 0 or j == sisi - 1 or l == 0 or l == sisi - 1:
                    print("*", end=" ")
                else: 
                    print(" ", end=" ")
        print()