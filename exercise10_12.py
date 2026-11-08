from pathlib import Path
import json

path = Path('angka_favorit.json')

if path.exists():
    isi = path.read_text()
    angka_favorit = json.loads(isi)
    print(f"Saya tahu angka favorit Anda! Angkanya adalah {angka_favorit}.")
else:
    print("Belum ada angka favorit yang tersimpan.")