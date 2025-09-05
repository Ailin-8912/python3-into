print("BELAJAR GIT DASAR")
print("-----------------")
# git init -> inisialisasi suatu  folder/projek ke git
import requests
kota = input("Masukkan nama kota : ")
url = f"https://api.aladhan.com/v1/timingsByCity/30-08-2025?city={kota}&country=Indonesia&method=8"
response = requests.get(url) # Http Get (ambil data)
data_json = response.json()
print(f"Jadwal Sholat {kota}")
print("-" * 40)
# print(data_json) 
# akses data sholat berdasarkan hirarki keys yang ada
# -> data -> timings -> keyNamaSholatNya
jadwal_sholat = data_json['data']['timings'] # versi ringkas (dipotong)
print(f"-> Shubuh = {jadwal_sholat['Fajr']}")
print(f"-> Dzuhur = {jadwal_sholat['Dhuhr']}")
print(f"-> Maghrib = {data_json['data']['timings']['Maghrib']}")