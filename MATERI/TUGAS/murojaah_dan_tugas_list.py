buah = ['apel', 'jeruk', 'Mangga', 'jeruk', 'durian', 'cherry']

# operasi pada list

# 1.) mengakses elemen [index = urutan]

print(buah[2])

# 2.) mengubah nilainya

buah[1] = "pisang"
print(buah)

# 3.) manambah elemen
# Diakhir

buah.append('semangka')
print(buah)

# di index terserah
buah.insert(4, 'anggur')
print(buah)

# 4.) menghapus elemen 
# menghapus berdasarkan isi

buah.remove('cherry')
print(buah)

# menghapus berdasarkan index

buah.pop(0)
print(buah)
 
 # 5.) panjang list 

print(len(buah))

# 6.) mencetakan seluruh isi list menggunakan looping

for item in buah:
    print(item)



# Tugasssss !!!!!!

# buat program yang :
# 1. minta user masukin 5 nama buah, satu persatu
# 2. nama nama buah yg tadi sudah di masukin oleh user,simpan kedalam list menggunakan append()
# 3. tampilkn nama nama buah yg telah antum masukan 

print("daftar buah")
list_buah = []

buah1 = input("masukan nama buah 1: ")
buah2 = input("masukan nama buah 2: ")
buah3 = input("masukan nama buah 3: ")
buah4 = input("masukan nama buah 4: ")
buah5 = input("masukan nama buah 5: ")

list_buah.append(buah1)
list_buah.append(buah2)
list_buah.append(buah3)
list_buah.append(buah4)
list_buah.append(buah5)

print(list_buah)

for item in list_buah:
    print(item)