print("Kalkulator Penjumlahan (Ketik 'q' untuk keluar).")

while True:
    angka_pertama = input("\nAngka pertama: ")
    if angka_pertama.lower() == 'q':
        break
        
    angka_kedua = input("Angka kedua: ")
    if angka_kedua.lower() == 'q':
        break
        
    try:
        hasil = int(angka_pertama) + int(angka_kedua)
    except ValueError:
        print("Maaf, mohon hanya masukkan angka (bukan teks).")
    else:
        print(f"Hasil penjumlahannya adalah: {hasil}")