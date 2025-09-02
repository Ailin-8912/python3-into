print("MATERI 9 - PYTHON 3 FUNCTION")
print("-----------------------------")
# function tidak akan di eksekusi jika tidak dipanggil
def say_hello(name):
  # print("Halo mr.", name) --> versi dengan koma
  # kasih f di awal string untuk menyisipkan variable/paramater
  # dengan diapit {nama_variabel}
  print(f"Halo mr. {name}")
  print("Baek baek aeee")

# lambda untuk menulis fungsi yang ringkas dengan 1 baris saja
# sering disebut juga fungsi anonim (tanpa nama)
# struktur [lambda] [parameter]: [isinya]
say_hello_mini = lambda name: print(f"Hello mr.{name}")
# panggil fungsi2nya di bawah ini
say_hello("Azzam")
say_hello("Syahid")
print("---------------->")
say_hello_mini("Wildan")
say_hello_mini("Harun")

# contoh penerapan lambda dengan higher-order function
jajan_mingguan = [50000, 30000, 70000, 10000, 45000, 15000]
# sorted() -> mengurutkan data
urutkan_uang = sorted(jajan_mingguan)
urutkan_uang_terbalik = sorted(jajan_mingguan, reverse=True)
print(f"Urutan Uang: {urutkan_uang}")
print(f"Urutan Uang Terbalik: {urutkan_uang_terbalik}")
# map() -> mentransformasi data
kurangin_uang = map(lambda uang: uang - 5000, jajan_mingguan)
# list() mengubah data objek map menjadi bentuk list
list_kurangin_uang = list(kurangin_uang) 
print(f"Map Uang berkurang: {list_kurangin_uang}")
# filter() -> menyaring / memfilter data
jajan_banyak = filter(lambda uang: uang >= 30000, jajan_mingguan)
list_jajan_banyak = list(jajan_banyak)
print(f"Filter jajan diatas 30rb: {list_jajan_banyak}")