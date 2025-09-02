print("hello world")
x = 10 * 5
y = 20 + 20
# operator += (y = y + 10)
y += 10
# operator -= (y = y - 5)
y -= 5
print(x, y)
# input() berguna menerima inputan dari user 
#nilaiumur = input("berapa umur mu?")
#print("umur kamu", "nilai umur", "tahun")

# if - else statement
# if (jika terpenuhi) - else (selainnya atau tidak terpenuhi)
# operator pembanding == != > <
print("masukan umur mu: ")
if ("nilai umur" == "25"):
    print ("umurnya ketuaan bang")
elif ("nilai umur" == "10"): # nilai umurnya adalah 10
    print("umurnya kemudaan dek")
else:
    print("umurnya cukup aja")

# operator != (tidak sama dengan)
kelasBudi = "A"
statuskelasBudi = kelasBudi != "C" # True
print("status kelas Budi: ", statuskelasBudi)

statuskehadiran = "hadir"
if (statuskehadiran != "Alpha"):
    print("mendapatkan point +1")
else: #statusnya Alpha 
    print("mendapatkan point -1")
# operator > (Lebih besar) dan < (Lebih kecil)
# sistem peringkat A (90 - 100), B (80 - 89), C (70 - 79), D (Selengkapnya)
nilaiujian = 90
print("nilai ujian: ", nilaiujian)
if (nilaiujian > 89 and nilaiujian <101):
    print("kamu peringkat A")
elif (nilaiujian > 79 and nilaiujian <90):
    print("kamu peringkat B")
else:
    print("kamu peringkat D")