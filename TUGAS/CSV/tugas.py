import csv

file_path = r"C:\belajar coding\semua_materi_python\materi 12\murojaah\TUGASSSSS\keuangan.csv"

with open(file_path, "r") as file_baru:
    next(file_baru)
    read = csv.reader(file_baru)
    list_read = list(read)

    print("- DATA KEUANGAN -")
    print("-"*50)
    for baris in list_read:
        tanggal = baris[0]
        keterangan = baris[1]
        kategori = baris[2]
        jumlah = baris[3]

        print(f"{tanggal} | {keterangan} | {kategori} | {jumlah}")