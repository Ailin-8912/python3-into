import csv
# Tambahkan moodule 'csv' dgn 'import'
print("Materi 11 - file handling part 2")
print("---------- UPDATE CSV ----------")
# baca isi file -> ekstrak data -> buat data baru 
# -> tulis ulang semua isi barisnya dengan mode 'w'
file_path_csv = r"C:\belajar coding\semua_materi_python\materi 10\jajan.csv"
# siapkan data jajan kosong 
# untuk menampung data dari csv ke list
data_jajan = []
# 1. baca seluruh data
with open(file_path_csv, "r") as file_jajan:
    # csv.reader() -> membaca isi file csv
    isi__table_jajan = csv.reader(file_jajan)
    # ekstrak semua da6a dengan for loop
    for item_jajan in isi__table_jajan:
        print(item_jajan)
        # tambah item ke list data data jajan 
        data_jajan.append(item_jajan)

# mengubah atau membuat data baru 
for item in data_jajan:
    print(f"proses item No => {item[0]}")
    print(item)
    # jika kolom nama (index 1) adalah "nama"
    if item[1] == "Thufail":
        uang_jajan_baru = 15000
        # ganti kolom uang (index 2) dengan nilai baru
        item[2] = 15000
        print(f"Data ditemukan, ganti uang jajan {uang_jajan_baru}")
    print("-------- Loop End --------")

print(f"DATA JAJAN TERKINI: {data_jajan}")

# hapus data di list index 2
del data_jajan[2]
print(f"DATA JAJAN TERKINI: {data_jajan}")
# 4. tulis ulang data dengan mode 'w' -> write 
with open(file_path_csv, "w", newline="") as file_jajan:
    writer = csv.writer(file_jajan)
    # .writerows() -> tulis sekali banyak
    writer.writerow(data_jajan)

print('---------------------------------------------------')

# contoh / ngulang function
# function biasa
def sapa():
    return "assalamualaikum"

print(sapa())

# Function dengan parameter

def sapaNama(nama, umur):
    return print(f"assalamualaikum, {nama}, umur kamu {umur}")

sapaNama("ucok", 15) # -> Argumen
