from pathlib import Path

path = Path('novel_contoh.txt')
path.write_text("The cat sat on the mat. Then the dog barked, and there was a sound.")

try:
    isi = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"File {path} tidak ditemukan.")
else:
    # 1. Menghitung 'the' secara umum (termasuk di dalam kata seperti 'then', 'there')
    jumlah_umum = isi.lower().count('the')
    print(f"Kata 'the' (termasuk di dalam kata lain) muncul sebanyak: {jumlah_umum} kali.")
    
    # 2. Menghitung 'the ' (menggunakan spasi di belakang untuk akurasi lebih tinggi)
    jumlah_spasi = isi.lower().count('the ')
    print(f"Kata 'the ' (dengan spasi) muncul sebanyak: {jumlah_spasi} kali.")