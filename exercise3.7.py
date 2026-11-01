guests = ['isaac newton', 'lee haechan', 'galileo galilei', 'marie curie', 'beomgyu', 'kimi', 'stephen curry']

print("Maaf semuanya, meja baru tidak tiba tepat waktu, jadi saya hanya bisa mengundang dua orang untuk makan malam.")

popped_guest = guests.pop()
print(f"Maaf {popped_guest.title()}, saya tidak dapat mengundang Anda ke makan malam.")

popped_guest = guests.pop()
print(f"Maaf {popped_guest.title()}, saya tidak dapat mengundang Anda ke makan malam.")

popped_guest = guests.pop()
print(f"Maaf {popped_guest.title()}, saya tidak dapat mengundang Anda ke makan malam.")

popped_guest = guests.pop()
print(f"Maaf {popped_guest.title()}, saya tidak dapat mengundang Anda ke makan malam.")

popped_guest = guests.pop()
print(f"Maaf {popped_guest.title()}, saya tidak dapat mengundang Anda ke makan malam.")

print(f"Halo {guests[0].title()}, Anda masih diundang untuk makan malam.")
print(f"Halo {guests[1].title()}, Anda masih diundang untuk makan malam.")

# Menggunakan del untuk menghapus dua nama terakhir dari daftar
del guests[0]
del guests[0]

print(guests)