current_users = ['budi', 'siti', 'admin', 'Joko', 'ani']
current_users_lower = [user.lower() for user in current_users]
new_users = ['joko', 'rina', 'SITi', 'eko', 'dewi']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Maaf, username '{new_user}' sudah digunakan. Anda harus memasukkan username baru.")
    else:
        print(f"Username '{new_user}' tersedia.")