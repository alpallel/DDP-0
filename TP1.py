import math

# Informasi perjalanan
jarak_tempuh = 0
koordinat_x_planet = 0
koordinat_y_planet = 0
durasi_perjalanan = 0
planet_saat_ini = "Bumi"
nama_rocket = ""
kecepatan_rocket = 0
menetap = False

# Informasi kriptografi
keyboard = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
len_keyboard = len(keyboard)

print(">>===================================================================<<")
print("||                                                                   ||")
print("||      🚀 SELAMAT DATANG DI DEK DEPE'S OUTER SPACE INTERFACE 🚀     ||")
print("||                                                                   ||")
print(">>===================================================================<<")

# Daftarkan roket
print("=" * 30, "Pendaftaran", "=" * 30)
print("\nDaftarkan Roket yang akan digunaka\n")
nama_rocket = input("Masukkan nama roket: ")
kecepatan_rocket = float(input("Masukkan kecepatan roket (km/s): "))
print("Roket", nama_rocket, "dengan kecepatan", kecepatan_rocket, "km/s telah didaftarkan.")

# Main program
while not menetap:

    print("=" * 29 + " Menu Utama " + "=" * 30)
    print()

    print("Lokasi saat ini:", planet_saat_ini) 
    print()
    print("Menu Utama:")
    print("1. Berangkat")
    print("2. Kirim Pesan")
    print("3. Baca Pesan")
    print("4. Lihat Laporan Perjalanan")
    print("5. Akhiri Perjalanan (keluar program)")

    print()
    pilihan = input("Masukkan pilihan: ")
    print()

    if pilihan == "1": # Berangkat ke planet tujuan
        print("=" * 30 + " Berangkat " + "=" * 30)
        print()
        
        while True:

            print("Pilih opsi navigasi:")
            print("1. Koordinat Kartesian (x, y)")
            print("2. Koordinat Polar (sudut, jarak)")
            print("3. Kembali ke Menu Utama")

            print()
            opsi_navigasi = input("Masukkan pilihan: ")
            print()

            if opsi_navigasi == "1": # Navigasi menggunakan koordinat kartesian

                # Terima input berupa koordinat dan nama planet
                planet_tujuan = input("Massukkan nama planet tujuan: ")
                koordinat_x_tujuan = int(input("Masukkan koordinat x planet tujuan: "))
                koordinat_y_tujuan = int(input("Masukkan koordinat y planet tujuan: "))

                # Hitung jarak tempuh dari koordinat dengan rumus Pythagoras
                jarak_tujuan = math.sqrt((koordinat_x_tujuan - koordinat_x_planet) ** 2 + (koordinat_y_tujuan - koordinat_y_planet) ** 2)
                jarak_tempuh += jarak_tujuan
                durasi_perjalanan +=  jarak_tujuan / kecepatan_rocket

                # Update koordinat planet saat ini
                koordinat_x_planet = koordinat_x_tujuan
                koordinat_y_planet = koordinat_y_tujuan

                # Update planet saat ini
                planet_saat_ini = planet_tujuan

                print()
                print("✅ Berhasil mendarat di Planet", planet_saat_ini)
                print()
                break
            
            elif opsi_navigasi == "2": # Navigasi menggunakan koordinat polar

                # Terima input berupa nama planet, sudut, dan jarak
                planet_tujuan = input("Masukkan nama planet tujuan: ")
                sudut_planet = int(input("Masukkkan sudut terhadap planet tujuan: "))
                jarak_tujuan = int(input("Masukkan jarak (dalam kilometer): "))

                # Konversi sudut ke radian
                sudut_planet = math.radians(sudut_planet)

                # Hitung koordinat x dan y planet tujuan
                koordinat_x_tujuan = koordinat_x_planet + jarak_tempuh * math.cos(sudut_planet)
                koordinat_y_tujuan = koordinat_y_planet + jarak_tempuh * math.sin(sudut_planet)

                koordinat_x_planet = koordinat_x_tujuan
                koordinat_y_planet = koordinat_y_tujuan

                # Update jarak tempuh dan durasi perjalanan
                jarak_tempuh += jarak_tujuan
                durasi_perjalanan +=  jarak_tujuan / kecepatan_rocket
                planet_saat_ini = planet_tujuan

                print()
                print("✅ Berhasil mendarat di Planet", planet_saat_ini)
                print()
                break

            elif opsi_navigasi == "3": # Kembali ke menu utama
                break
            
            else:
                print("Mohon pilih opsi yang valid")
                print()
                continue

    elif pilihan == "2": # Kirim pesan menggunakan metode enkripsi
        print("=" * 25 + " Kirim Pesan Ke Bumi " + "=" * 25)
        print()

        while True:
            print("Metode Enkripsi:")
            print("1. Enkripsi berdasarkan Jarak Tempuh")
            print("2. Enkripsi berdasarkan Nama Planet Saat Ini")
            print("3. Enkripsi Biner")
            print("4. Enkripsi Heksadesimal")
            print("5. Enkripsi Membalik")
            print("6. Kembali ke Menu Utama")
            
            print()
            opsi_enkripsi = input("Masukkan pilihan: ")
            print()

            if opsi_enkripsi == "1": # Enkripsi berdasarkan jarak tempuh
                pesan = input("Masukkan pesan yang ingin dikirim: ")
                pesan_terenkripsi = ""

                for karakter in pesan:
                    int_index = 0
                    for index in range(len(keyboard)):
                        if karakter == keyboard[index]:
                            int_index = index
                            break
                    pesan_terenkripsi += keyboard[(int_index + int(jarak_tempuh)) % len_keyboard]

                print()    
                print('Hasil Enkripsi: """' + pesan_terenkripsi + '"""')
                print()
                break

            elif opsi_enkripsi == "2": # Enkripsi berdasarkan nama planet saat ini
                pesan = input("Masukkan pesan yang ingin dikirim: ")
                pesan_terenkripsi = ""

                for index_karakter1 in range(len(pesan)):
                    karakter1 = pesan[index_karakter1]

                    for index_karakter2 in range(len(planet_saat_ini)):
                        karakter2 = planet_saat_ini[index_karakter2]
                        alphabet_index1 = 0
                        alphabet_index2 = 0

                        for index in range(len_keyboard):
                            if keyboard[index] == karakter1:
                                alphabet_index1 = index
                            if keyboard[index] == karakter2:
                                alphabet_index2 = index

                        pesan_terenkripsi += keyboard[(alphabet_index1 + alphabet_index2) % len_keyboard]
                
                print()
                print('Hasil Enkripsi: """' + pesan_terenkripsi + '"""')
                print()
                break

            elif opsi_enkripsi == "3": # Enkripsi Biner
                pesan = input("Masukkan pesan yang ingin dikirim: ")
                pesan_terenkripsi = ""

                for karakter3 in pesan:
                    int_index = 0
                    for index in range(len(keyboard)):
                        if karakter3 == keyboard[index]:
                            int_index = index
                            break

                    binary_string = ""
                    backup_int_index = int_index

                    while backup_int_index != 0:
                        if backup_int_index % 2 == 0:
                            binary_string = "0" + binary_string
                        else:
                            binary_string = "1" + binary_string

                        backup_int_index //= 2
                    
                    if binary_string == "":
                        binary_string = "0" * 8

                    len_binary_string = len(binary_string)
                    sign_extend = "0" * (8 - len_binary_string)
                    binary_string = sign_extend + binary_string
                    pesan_terenkripsi += binary_string
                
                print()
                print('Hasil Enkripsi: """' + pesan_terenkripsi + '"""')
                print()
                break
                    
            elif opsi_enkripsi == "4": # Enkripsi Heksadesimal
                pesan = input("Masukkan pesan yang ingin dikirim: ")
                pesan_terenkripsi = ""

                for karakter4 in pesan:
                    int_index = 0
                    for index in range(len(keyboard)):
                        if karakter4 == keyboard[index]:
                            int_index = index
                            break
                    
                    hexadecimal_string = ""
                    backup_int_index = int_index

                    while backup_int_index != 0:
                        int_hexadecimal_in_decimal = backup_int_index % 16

                        if int_hexadecimal_in_decimal <= 9:
                            hexadecimal_string = str(int_hexadecimal_in_decimal) + hexadecimal_string

                        else:
                            hexadecimal_string = chr(55 + int_hexadecimal_in_decimal) + hexadecimal_string
                        
                        backup_int_index //= 16
                    
                    if hexadecimal_string == "":
                        hexadecimal_string = "0" * 2
                    
                    len_hexadecimal_string = len(hexadecimal_string)                 
                    sign_extend = "0" * (2 - len_hexadecimal_string)
                    hexadecimal_string = sign_extend + hexadecimal_string               
                    pesan_terenkripsi += hexadecimal_string
                
                print()
                print('Hasil Enkripsi: """' + pesan_terenkripsi + '"""')
                print()
                break

            elif opsi_enkripsi == "5":    # Enkripsi Membalik           
                pesan = input("Masukkan pesan yang ingin dikirim: ")
                pesan_terenkripsi = pesan[::-1]

                print()
                print('Hasil Enkripsi: """' + pesan_terenkripsi + '"""')
                print()
                break

            elif opsi_enkripsi == "6": # Kembali ke menu utama
                break

            else:
                print("Mohon pilih opsi yang valid")
                print()
        
    elif pilihan == "3": # Baca pesan yang telah dikirim menggunakan metode dekripsi

        print("=" * 29 + " Baca Pesan " + "=" * 30)
        print()

        while True:

            print("Metode Dekripsi:")
            print("1. Dekripsi berdasarkan Jarak Tempuh")
            print("2. Dekripsi berdasarkan Nama Planet Saat Ini")
            print("3. Dekripsi Biner")
            print("4. Dekripsi Heksadesimal")
            print("5. Dekripsi Membalik")
            print("6. Dekripsi Brute Force (Jarak Tempuh)")
            print("7. Dekripsi Brute Force (Nama Planet)")
            print("8. Kembali ke Menu Utama")
            
            print()
            opsi_dekripsi = input("Masukkan pilihan: ")
            print()

            if opsi_dekripsi == "1": # Dekripsi berdasarkan jarak tempuh
                pesan_terenkripsi = input("Masukkan pesan terenkripsi yang ingin dibaca: ")
                pesan_dekripsi = ""

                for karakter1 in pesan_terenkripsi:                  
                    int_index = 0

                    for index in range(len(keyboard)):
                        if karakter1 == keyboard[index]:
                            int_index = index
                            break
                    
                    pesan_dekripsi += keyboard[(int_index - int(jarak_tempuh)) % len_keyboard]

                print()    
                print('Hasil Dekripsi: """' + pesan_dekripsi + '"""')
                print()
                break
            
            elif opsi_dekripsi == "2": # Dekripsi berdasarkan nama planet saat ini

                pesan_terenkripsi = input("Masukkan pesan terenkripsi yang ingin dibaca: ")
                pesan_dekripsi = ""

                len_pesan_terenkripsi = len(pesan_terenkripsi)
                len_planet_saat_ini = len(planet_saat_ini)        

                key_character = planet_saat_ini[0]
                key_character_index = 0

                for index in range(len(keyboard)):
                    if key_character == keyboard[index]:
                        key_character_index = index
                        break

                for karakter1_index in range(0, len_pesan_terenkripsi, len_planet_saat_ini):
                    
                    karakter1 = pesan_terenkripsi[karakter1_index]
                    alphabet_index1 = 0

                    for index in range(len(keyboard)):
                        if karakter1 == keyboard[index]:
                            alphabet_index1 = index
                            break

                    pesan_dekripsi += keyboard[(alphabet_index1 - key_character_index) % len_keyboard]

                print()        
                print('Hasil Dekripsi: """' + pesan_dekripsi + '"""')
                print()
                break
            
            elif opsi_dekripsi == "3": # Dekripsi Biner
                
                pesan_terenkripsi = input("Masukkan pesan terenkripsi yang ingin dibaca: ")
                pesan_dekripsi = ""

                for index_karakter4 in range(0, len(pesan_terenkripsi), 8):

                    binary_coded_character = pesan_terenkripsi[index_karakter4:index_karakter4+8]
                    index_coded_character = 0

                    for binary_digit in range(8):
                        index_coded_character += int(binary_coded_character[binary_digit]) * (2 ** (7 - binary_digit))
                    
                    pesan_dekripsi += keyboard[index_coded_character]
                
                print()
                print('Hasil Dekripsi: """' + pesan_dekripsi + '"""')
                print()
                break
            
            elif opsi_dekripsi == "4": # Dekripsi Heksadesimal
                
                pesan_terenkripsi = input("Masukkan pesan terenkripsi yang ingin dibaca: ")
                pesan_dekripsi = ""

                for index_karakter5 in range(0, len(pesan_terenkripsi), 2):

                    hexadecimal_coded_character = pesan_terenkripsi[index_karakter5:index_karakter5+2]
                    index_coded_character = 0

                    for hexadecimal_digit in range(2):
                        actual_hexadecimal_digit = hexadecimal_coded_character[hexadecimal_digit]

                        if actual_hexadecimal_digit.isdigit():
                            index_coded_character += int(actual_hexadecimal_digit) * (16 ** (1 - hexadecimal_digit))

                        else:
                            index_coded_character += (ord(actual_hexadecimal_digit) - 55) * (16 ** (1 - hexadecimal_digit))

                    pesan_dekripsi += keyboard[index_coded_character]
                
                print()
                print('Hasil Dekripsi: """' + pesan_dekripsi + '"""')
                print()
                break

            elif opsi_dekripsi == "5": # Dekripsi Membalik

                pesan_terenkripsi = input("Masukkan pesan terenkripsi yang ingin dibaca: ")
                pesan_dekripsi = pesan_terenkripsi[::-1]

                print()
                print('Hasil Dekripsi: """' + pesan_dekripsi + '"""')
                print()
                break

            elif opsi_dekripsi == "6": # Algoritma dekripsi brute force berdasarkan jarak tempuh (angka)

                # Terima pesan yang diingin didekripsi oleh pengguna
                int_decryption_counter = 1
                string_input = input("Masukkan pesan terenkripsi yang ingin dibaca: ")
                print()

                # TODO:
                # Karena terdapat 95 karakter pada keyboard, sebuah algoritma dekripsi brute force Caesar cipher
                # perlu cek semua 95 shift yang memungkinkan
                for integer_shift in range(...):

                    # Siapkan string_output sebagai string hasil dekripsi
                    string_output = ""

                    # Akses semua karakter pada string_input
                    for karakter in string_input:

                        # TODO:
                        # Cari indeks karakter
                        # sesuai dengan kolom "Urutan ke-" di
                        # "Subbab 17.2: Alfabet Aplikasi Dek Depe's Outer Space Interface"
                        # pada Google Doc TP1 DDP-0 2025
                        int_index = 0
                        for index in range(len(keyboard)):
                            if karakter == keyboard[...]:
                                int_index = ...
                                break
                        
                        # TODO:
                        # Kurangi int_index dengan integer_shift dan tambahkan karakter
                        # dengan urutan tersebut pada keyboard ke string_output
                        string_output += keyboard[(... - ...) % len_keyboard]
                    
                    # Tunjukkan hasil dari upaya dekripsi saat ini kepada pengguna
                    print('Upaya Dekripsi ' + str(int_decryption_counter) + ': """' + string_output + '"""')
                    int_decryption_counter += 1

                print()
                break

            elif opsi_dekripsi == "7": # Algoritma dekripsi brute force berdasarkan nama planet (string)

                # Terima pesan yang diingin didekripsi oleh pengguna
                int_decryption_counter = 1
                string_input1 = input("Masukkan pesan terenkripsi yang ingin dibaca: ")
                print()

                # Misal m = panjang dari teks sebelum enkripsi
                #       n = panjang dari string yang digunakan pada enkripsi modified Vigenere cipher
                # Perhatikan bahwa panjang dari teks setelah dienkripsi = m * n
                # Gunakan fakta ini untuk mendekripsikan teks yang telah dienkripsikan oleh modified Vigenere cipher

                # Taruh nilai dari panjang string_input1 pada sebuah variabel
                len_string_input1 = len(string_input1)

                # TODO:
                for angka in range(1, ...+1):

                    # Apabila angka merupakan faktor dari len_string_input1,
                    # angka tersebut dapat menjadi panjang dari string yang digunakan untuk mengenkripsikan
                    # teks asli (teks sebelum dienkripsi).

                    # Apabila angka bukan faktor dari len_string_input1,
                    # lanjut ke angka berikut.

                    # TODO:
                    if ... % ... == 0:
                        
                        # TODO:
                        # Untuk setiap angka yang merupakan faktor dari len_string_input1,
                        # terdapat 95 karakter yang dapat menjadi karakter yang mengenkripsikan teks asli.
                        for character_integer in range(...):
                        
                            string_output = ""

                            # TODO:
                            for karakter in range(0, ..., ...):
                                
                                karakter_string_input1 = string_input1[karakter]

                                # Cari indeks karakter
                                # sesuai dengan kolom "Urutan ke-" di
                                # "Subbab 17.2: Alfabet Aplikasi Dek Depe's Outer Space Interface"
                                # pada Google Doc TP1 DDP-0 2025
                                alphabet_index1 = 0
                                for index in range(len(keyboard)):
                                    if karakter_string_input1 == keyboard[index]:
                                        alphabet_index1 = index
                                        break

                                # TODO:
                                # Kurangi alphabet_index1 dengan character_integer dan tambahkan karakter
                                # dengan urutan tersebut pada keyboard ke string_output
                                string_output += keyboard[(... - ...) % len_keyboard]
                                    
                            # Tunjukkan hasil dari upaya dekripsi saat ini kepada pengguna        
                            print('Upaya Dekripsi ' + str(int_decryption_counter) + ': """' + string_output+'"""')
                            int_decryption_counter += 1
                
                print()
                break
            
            elif opsi_dekripsi == "8": 
                break
            
            else: 
                print("Mohon pilih opsi yang valid")
                print()
                continue
        
    elif pilihan == "4":

        # Tampilkan output laporan perjalanan
        print("="*25 + " Laporan Perjalanan " + "="*26)
        print()


        print("Nama Roket:", nama_rocket)
        print("Kecepatan Roket:", kecepatan_rocket, "km/s")
        print("Jarak Tempuh:", jarak_tempuh, "km")
        print("Durasi Perjalanan:", durasi_perjalanan, "detik")
        
        print()
        print("=" * 22 + " Informasi Lokasi Saat Ini "  + "=" * 22)
        print()
        
        print("Planet Saat Ini:", planet_saat_ini)

        jarak_bumi = math.sqrt(koordinat_x_planet ** 2 + koordinat_y_planet ** 2)

        print("Jarak Planet dari Bumi:", jarak_bumi, "km")
        
        sudut_planet = math.degrees(math.atan(float(koordinat_y_planet) / float(koordinat_x_planet)))

        if sudut_planet < 0:
            sudut_planet += 360

        print("Sudut Planet dari Bumi:", sudut_planet, "derajat")
        print()

    elif pilihan == "5": # Akhiri perjalanan
        menetap = True

        print("=" * 26 + " Akhiri Perjalanan " + "=" * 26)
        print()
        print("Selamat menetap di Planet", planet_saat_ini)
        print()
        print("=" * 71)
        print()
    
    else: # Apabila input tidak valid
        print("Mohon pilih opsi yang valid")
        print()