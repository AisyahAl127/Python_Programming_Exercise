from pathlib import Path
import json

# Meminta input angka favorit dari pengguna
angka_favorit = input("Berapa angka favorit Anda? ")

# Menentukan path file JSON
path = Path('angka_favorit.json')

# Mengonversi angka menjadi string JSON dan menyimpannya ke file
isi = json.dumps(angka_favorit)
path.write_text(isi)

print("Angka favorit Anda telah disimpan!")