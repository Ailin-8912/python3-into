print("Hello world")

# Tugas pekanan : Tanggal 02 agustus 2025

print("=== PROFIL DIGITAL PRIBADI ===")

nama = input("nama lengkap:")
umur = int(input("umur:"))
hitung_umur = 2025 - umur
print("tahun:",hitung_umur)
kelas = input("kelas:")
cita_cita = input("cita-cita:")
hobi = input("hobi:")
waktubelajar = input("lebih suka belajar siang apa malam? :")

print("=== TIPE GAYA DIGITAL ===")

print("Pilih tipe gaya digital mu (ketik angkanya aja)")
print("1. Wibu (Anak anime banget)")
print("2. Gamer (Ranked jalan terus)")
print("3. K-Popers (Ngikutin gaya Korea)")
print("4. Anak konten (Tiktoker/Youtuber wannabe)")
print("5. Anak nongki (Yang penting ngumpul)")
tipe = input("pilih tipe digital kamu (1-5):")
if tipe == "1":
    pertanyaan_tambahan = "Siapa waifu atau husbando kamu?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ")
    komentar = input("sorry gw gak terlalu ngerti ginian")
elif tipe == "2":
    pertanyaan_tambahan = "Game favorit kamu apa?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ")
    komentar = input("widih pasti jago !!!")
elif tipe == "3":
    pertanyaan_tambahan = "Siapa bias kamu?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ")
    komentar = input("sorry gw gak ngerti ginian")
elif tipe == "4":
    pertanyaan_tambahan = "Platform favorit kamu? TikTok? YouTube?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ").lower()

    if jawaban_tambahan == "tiktok":
        print(" sorry gw gak main tiktok!")
    else:
        print("gw seringnya IG ~")
elif tipe == "5":
    pertanyaan_tambahan = "Nongkrong paling sering di mana?"
    jawaban_tambahan = input(pertanyaan_tambahan + " ")
    komentar = input("sorry gw gk tau, soalnya gw ga pernah nongkrong")
else:

    jawaban_tambahan = "Tidak ada jawaban"

print("Jawab pertanyaan bonus ini :> :")
jawaban = input("Apakah teman di sebelah kamu bau? (ya/Ga): ")

if jawaban == "ya":
    print("Waduh '-' ! suruh mandi dulu sana~")
elif jawaban == "Ga":
    print("Syukur ( -.-') deh... ~")
else:
    print(" Jawab yang bener dong, ya atau Ga aja -_- ~")    

print("-==== SELESAI ====-")