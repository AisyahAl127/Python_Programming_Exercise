from pathlib import Path

nama = input("Masukkan nama Anda: ")

path = Path('tamu.txt')

path.write_text(nama)

print(f"Nama '{nama}' telah berhasil disimpan ke dalam file tamu.txt.")