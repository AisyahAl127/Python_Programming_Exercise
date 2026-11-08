print("Masukkan dua angka untuk dijumlahkan.")
angka_pertama = input("Angka pertama: ")
angka_kedua = input("Angka kedua: ")

try:
    hasil = int(angka_pertama) + int(angka_kedua)
except ValueError:
    print("Maaf, Anda memasukkan teks, bukan angka yang valid.")
else:
    print(f"Hasil penjumlahannya adalah: {hasil}")