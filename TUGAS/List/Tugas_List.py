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