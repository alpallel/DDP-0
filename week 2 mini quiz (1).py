dataIkan = [
["Ikan Lele", "Clarias batrachus", "Clariidae"],
["Ikan Gurame", "Osphronemus goramy", "Osphronemidae"],
["Ikan Cupang", "Betta splendens", "Osphronemidae"]]

kategori = ["Nama Ikan", "Nama Ilmiah", "Nama Genus", "Nama Family"]

for i in range(len(dataIkan)):
    nama_ilmiah = dataIkan[i][1].split()[0]
    dataIkan[i].insert(2, nama_ilmiah)

for i in range(len(kategori)):
    print(f"{kategori[i]:<15}", end="|")

    for j in range(len(dataIkan)):
        print(f"{dataIkan[j][i]:^20}", end="|")
    print()