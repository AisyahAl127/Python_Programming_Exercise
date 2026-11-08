from pathlib import Path

nama_file = ['cats.txt', 'dogs.txt', 'hamsters.txt'] 

for filename in nama_file:
    path = Path(filename)
    print(f"\n--- Membaca file: {filename} ---")
    try:
        isi = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass # Gagal diwujudkan tanpa mencetak pesan apa pun
    else:
        print(isi.strip())