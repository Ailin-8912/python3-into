# Tugas list[]

piket_hari_ini = ["Dzaky","Dihyah","Royan","Ziyad"]
print("Jadwal Piket Hari ini adalah:")
for jadwal in piket_hari_ini:
    print('-',jadwal)

# Tugas Tuple
print(" ")
rukun_islam = ('Syahadat', 'Shalat', 'Zakat', 'Puasa', 'Haji')
print("rukun islam :")
for i in rukun_islam:
    print(f"- {i}")

print(" ")
rukun_iman = (
    'Iman kpd Allah',
    'Iman kpd Malaikat',
    'Iman kpd Kitab', 
    'Iman kpd Rasul', 
    'Iman kpd Hari Akhir', 
    'Iman kpd Takdir'
      )

print("Rukun Iman :")
for i in range(len(rukun_iman)):
    print(f"{i + 1}. {rukun_iman[i]}")

#4
print(" ")
print("Kitab yang dimiliki : ")
kitab = {'Kitab Tajwid','kitab Tauhid','Kitab Al-Quran',}
for bukubuku in kitab:
    print('-',bukubuku)


#5
bioData1 = {
    "nama":"Rafi",
    "Asal":'Jakarta',
    'umur':'16',
    'kelas':'X SMA',
    'hobi':'Membaca Buku',
    'sifat': {
        'sifat1':'rajin',
        'sifat2':'semangat',
        'sifat3':'disiplin',
        'sifat4':'patuh'
    }}
print("")
print("Biodata santri: ")
print("")
print("Nama: ",bioData1 ["nama"])
print("Kelas: ",bioData1["kelas"])
print("Asal: ",bioData1["Asal"])
print("Umur: ",bioData1["umur"])
print("Hobi: ",bioData1["hobi"])
print("Sifat2 yg dimiliki : ",bioData1["sifat"]["sifat1"],",",bioData1['sifat']['sifat2'],",",bioData1['sifat']['sifat3'],",",bioData1['sifat']['sifat4'])

