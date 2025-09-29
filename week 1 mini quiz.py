number = int(input("Masukkan bilangan bulat: "))

while number > 0:
    i = number
    while i > 0:
        print(number, end=" ")
        i -= 1
    number -= 1
    print()
