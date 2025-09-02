print("---------------------------")

# Set -> { } -> tidak berurutan, berubah, tidak duplikat
game_azka = {"valorant", "delta", "roblox", "cod"}
game_zaky = {"minecraf", "roblox"}
game_zaky.add('minecraft')
game_zaky.add('roblox')
game_azka.add('minecraft')
game_azka.add('roblox')
game_azka.remove('delta')

print("game azka :", game_azka)
print("game zaky : ", game_zaky)
game_gabungan = game_azka | game_zaky # | -> (or) atau
print("daftar game : ", game_gabungan)

# for (loop) untuk mengeluarkan isi itemdari set
for game in game_gabungan:
    print(game)
    print('---> transfer data game', game, 'PS5')

# Dictionary (dict) -> {key : value} / {kunci : nilai} -> berurutan, berubah, tidak duplikat

kamus_anime = {
    "key": "value",
    "one_piece": "Monkey D Luffy",
    "blue_lock": "Isagi ren",
    "demon_slayer":  "Tanjiro",
    "waifu": {
        "one_piece": "big mom",
        "demon_slayer": "nezuko",
    }
}
print("kamus anime : ", kamus_anime)
print("MC demon slayer : ", kamus_anime["demon_slayer"])
print("waifu one piece : ", kamus_anime["waifu"]["one_piece"])

# nambah item baru ke dictionary
kamus_anime["naruto"] = "shikamaru"
print("MC naruto:", kamus_anime["naruto"])
# mengubah item dari dictionary
kamus_anime["demon_slayer"] = "zenitsu"
# menghapus item dari dictionary
del(kamus_anime['blue_lock'])
print("kamus anime terbaru: ", kamus_anime)