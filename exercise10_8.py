from pathlib import Path

Path('cats.txt').write_text("Whiskers\nShadow\nLuna\n")
Path('dogs.txt').write_text("Buddy\nMax\nCharlie\n")

nama_file = ['cats.txt', 'dogs.txt']

for filename in nama_file:
    path = Path(filename)
    print(f"\n--- Membaca file: {filename} ---")
    try:
        isi = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.")
    else:
        print(isi.strip())