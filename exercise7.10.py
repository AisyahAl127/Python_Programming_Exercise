responses = {}

polling_aktif = True

while polling_aktif:
    nama = input("\n Nama: ")
    response = input("Tempat yang ingin dikunjungi: ")
    
    responses[nama] = response
    
    repeat = input("Apakah Anda ingin membiarkan orang lain merespons? (ya/tidak) ")
    if repeat == 'tidak':
        polling_aktif = False

print("\n--- Hasil Polling Liburan Impian ---")
for nama, response in responses.items():
    print(f"{nama} ingin sekali mengunjungi {response}.")