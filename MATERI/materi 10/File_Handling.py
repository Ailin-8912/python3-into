import csv

print("Materi 10 - File Handling")
print("-------------------------")
# buka file
file_path = r"C:\belajar coding\semua_materi_python\materi 10\pesan.txt" # sesuaikan sendiri
file_pesan = open(file_path, "r")
# baca isi file
isi_pesan = file_pesan.read()
# tampilkan output isi pesan
print(f"ISI PESAN => {isi_pesan}")
# tutup file
file_pesan.close()

print('-----READ CSV FILE -----')
print("--------------------------")
file_path_csv = r"C:\belajar coding\semua_materi_python\materi 10\jajan.csv"
file_jajan = open(file_path_csv, "r")
isi_table_jajan = file_jajan.read()
print(f"TABLE JAJAN => {isi_table_jajan}")
file_jajan.close()

print('-----APPEND CSV FILE -----')
jajan_baru = [6,"Syahid",100000]
print(f"Jajan baru: {jajan_baru}")
# open() -> membuka file dati path
# mode 'a' -> append (tambah data)
# newline -> tambah baris baru dengan teks kosong
# with ... as -> buka file dengan tutup otomatis  
with open(file_path_csv, "a", newline="") as file_jajan:
  # aktifkan mode writer csv dari file target
  writer = csv.writer(file_jajan)
  # tambahkan baris dari variable jajan baru
  writer.writerow(jajan_baru)

