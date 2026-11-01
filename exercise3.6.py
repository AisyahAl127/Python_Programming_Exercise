guests = ['lee haechan', 'marie curie', 'beomgyu', 'kimi']

print("Halo semuanya, saya menemukan meja makan yang lebih besar!")

guests.insert(0, 'isaac newton')       # angka 0 menunjukan posisi penambahan list
guests.insert(2, 'galileo galilei')    
guests.append('stephen curry')       

# Mencetak set pesan undangan yang baru untuk setiap orang di daftar
print(f"Halo {guests[0].title()}, Anda diundang untuk makan malam bersama saya.")
print(f"Halo {guests[1].title()}, Anda diundang untuk makan malam bersama saya.")
print(f"Halo {guests[2].title()}, Anda diundang untuk makan malam bersama saya.")
print(f"Halo {guests[3].title()}, Anda diundang untuk makan malam bersama saya.")
print(f"Halo {guests[4].title()}, Anda diundang untuk makan malam bersama saya.")
print(f"Halo {guests[5].title()}, Anda diundang untuk makan malam bersama saya.")
print(f"Halo {guests[6].title()}, Anda diundang untuk makan malam bersama saya.")
print (guests)
