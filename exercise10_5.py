from pathlib import Path

print("Ketik 'keluar' jika sudah selesai memasukkan nama.\n")

path = Path(r'bukutamu.txt')
daftar_tamu = ""

while True:
    nama = input("Masukkan nama tamu: ")
    
    if nama.lower() in ['keluar']:
        break
    
    daftar_tamu += f"{nama}\n"
    print(f"Halo {nama}, kehadiran Anda telah dicatat.")

path.write_text(daftar_tamu)

print("\nSemua nama tamu telah berhasil disimpan ke dalam file bukutamu.txt.")