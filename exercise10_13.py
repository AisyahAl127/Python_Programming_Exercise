from pathlib import Path
import json

path = Path('profil_pengguna.json')

if path.exists():
    isi = path.read_text()
    profil = json.loads(isi)
    print("Selamat datang kembali! Berikut informasi yang kami ingat tentang Anda:")
    for kunci, nilai in profil.items():
        print(f"- {kunci.title()}: {nilai}")
else:
    profil = {}
    profil['nama'] = input("Siapa nama Anda? ")
    profil['usia'] = input("Berapa usia Anda? ")
    profil['hobi'] = input("Apa hobi utama Anda? ")
    
    isi = json.dumps(profil)
    path.write_text(isi)
    print("Data profil Anda telah disimpan. Kami akan mengingatnya!")
    