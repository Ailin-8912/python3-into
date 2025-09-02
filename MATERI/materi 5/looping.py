print("Hello, Rawr !!!")

#For loop (index dimulai dari 0 sampai 5)
for angka in range(0, 5):
    print("halo ke-", angka)
    print("mantap !")
print("--- selesai ---") # ini gak akan masuk ke loop karna diluar blok kode    

# for loop ke string
sandiwifi = "hsijoglo"
for huruf in sandiwifi:
    print(huruf,"==>")

# While loop (ulangi sampai kondisi terpenuhi)
no = 1 
batas = 10
while(no < batas):
    #print("ulangi ke-", no)
    print("*"* no)
    no += 1 
# kalau looping berjalan terus tekan ctrl + c untuk membatalkan eksekusi program / memberhentikan program

# simulasi flowchart cek umur sim 
print("--- mulai ---")
cekumur= input("berapa umur anda ?")
# konversi / menggantitipe data suatu variable
#fungsi int() mengganti string ke integer
angkaumur = int (cekumur)
if (angkaumur >=18):
    print("selamat anda bisa buat sim")
else:
    print("masih kecil pulang aja sana !!!")

print("--- selesai ---")
