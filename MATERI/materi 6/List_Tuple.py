print("Materi 6 - python data structure")
print("--------------------------------")
print("------ LIST ------")
# List [] (berurutan, bisa di ubah, boleh di duplikat)
daftar_belanja = [
    "teh desa", # index 0
    "molen", # index 1
    "pisang kembung", # index 2
]
# mengakses lewat index
print("isi tas belanja:", daftar_belanja)
print("item ke-1", daftar_belanja[0])
print("item ke-2", daftar_belanja[1])
# append() menambah item baru ke akhir list
daftar_belanja.append("olive chicken")
daftar_belanja.append("gabin")
print("isi tas belanja sekarang:", daftar_belanja)
print("item ke-4", daftar_belanja[3])
# remove() menghapus item dari list 
daftar_belanja.remove("pisang kembung")
print("isi tas belanja akhir:", daftar_belanja)

print("------ TUPLE ------")
# tuple (berurut, tidak bisa diubah, boleh duplikat)
# penulisannya menggunakan ()
tempat_tgl_lahir = ("cirebon", 8, "mei", 2011)
print("Tanggal lahir Fahri", tempat_tgl_lahir)
# [no_index] akses data tuple
print("tempat:", tempat_tgl_lahir[0])
print("Tanggal", tempat_tgl_lahir[1])
print("Bulan:", tempat_tgl_lahir[2])
print("Tahun:", tempat_tgl_lahir[3])
# akses bulan (posisi index) : lalu batas akhir itemnya 
print("Bulan Tahun:", tempat_tgl_lahir[2:4] )
# Unpacking tuple ke variable baru
# menguruti urutan itemnya
tempat_lahir, tgl_lahir, bulan_lahir, thn_lahir = tempat_tgl_lahir
print(tempat_lahir) 

# manipulasi list lanjutan 
jajan_ujang = ["pentol", "cireng"]
jajan_asep = ["bakso", "nasgor"]
jajan_ujang_dan_asep = jajan_ujang + jajan_asep
print(jajan_ujang_dan_asep)
# list multi-dimensi
list_minuman = [
    ["kopi", "susu", "teh"], # baris 0
    ["jus apel", "jus melon", "jus jeruk"], # baris 1
    ["es teler", "es campur", "es dawet"]
]
print(list_minuman)
# tiap baris punya 3 index ( 0, 1, 2)
print(list_minuman[0][2]) # akses es campur

