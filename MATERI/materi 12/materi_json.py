import json
# tambahkan module 'json' dengan 'import'
print("Materi 12 - JSON File Handling")
print("---------- READ JSON ----------")
file_path_json = r"C:\belajar coding\semua_materi_python\materi 12\materi.json"
with open(file_path_json, "r") as file_materi:
    # json.load() -> membaca isi file json 
    data_materi = json.load(file_materi)
   # keys: title, total, status_santri, status_lulus, pelajaran
    # akses data json dengan 'key' nya 
    print(f"judul berkas: {data_materi['title']}")
    print(f"total kelas A: {data_materi['total']}")
    print(f"status santri: {data_materi['status_santri']}")
    print(f"status kelulusan: {data_materi['status_lulus']}")
    # ekstak data list dengan for loop
    for pelajaran in data_materi['pelajaran']:
        print(f"--> {pelajaran}")
    # ekstrak semua data array object suarh
    # di python disebut juga  list of dictionary
    # keys surah: no, nama, ayat, turun
    print("-"*50) # Gandakan simbol dgn perkalian
    print("| No | Nama Surah | Ayat | Tempat Turun |") 
    print("-"*50)
    for surah in data_materi['surah']:
        print(f"| {surah['no']} | {surah['nama']} | {surah['ayat']} | {surah['turun']}")