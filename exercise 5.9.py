#Daftar username jika tidak ada pengguna
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {username.title()}, terima kasih sudah masuk kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")