import math 
from math import pi, sqrt 

print("==SELAMAT DATANG DI FORM PENDAFTARAN EXPEDISI== \n\n==DATA KAPTEN==")
Nama_Kapten = input ("Nama Kapten: ")
Tanggal_Lahir = input("Tanggal Lahir: ")
Tinggi_Badan = input("Tinggi Badan: ")
Tempat_Tinggal = input("Tempat Tinggal: ")
Zodiak = input("Zodiak: ")

print("\n==DATA ROKET==\n")
Nama_Roket = input("Nama Roket: ")
Tinggi_Roket = int(input("Tinggi Roket: "))
Tujuan_Ekspedisi = input("Tujuan Ekspedisi: ")

t = Tinggi_Roket / 2 #Rumus lama waktu berlalu setelah roket lepas landas
Kecepatan_Roket = pi * t ** 2 + sqrt(2) * t #Rumus kecepatan roket

print("\nTerdaftar! Kapten Anda adalah", Nama_Kapten, "yang berasal dari", Tempat_Tinggal + 
      ". Tanggal lahir kapten anda adalah", Tanggal_Lahir, "dan memiliki tinggi badan", 
      Tinggi_Badan, " cm. Zodiak kapten anda adalah", Zodiak + ". Anda ingin berekspedisi ke", 
      Tujuan_Ekspedisi, "menggunakan roket", Nama_Roket, "yang memiliki tinggi", str(Tinggi_Roket) + " m.", 
      "Roket Anda akan mencapai kecepatan", Kecepatan_Roket, "m/s selama 50 detik setelah lepas landas."
      "\n\n=== TERIMA KASIH TELAH MENDAFTAR! SELAMAT MENJELAJAH! ===")