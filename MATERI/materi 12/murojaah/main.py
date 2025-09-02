import csv

file_path = r"C:\belajar coding\semua_materi_python\materi 12\murojaah\data.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)

    print("Semua DATA")
    print("-" * 20)
    for baris in list_read:
        nomor = baris[0]
        nama = baris [1]
        kelas = baris[2]

        print(f"{nomor} | {nama} | {kelas}")

# Tambah Data
with open(file_path, "a", newline="") as file_baru:
    write = csv.writer(file_baru)
    write.writerow(["5", "Syahid", "10"])