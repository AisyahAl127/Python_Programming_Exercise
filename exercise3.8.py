places = ['jepang', 'swiss', 'selandia baru', 'norwegia', 'kanada']

print("Urutan asli:")
print(places)

#urutan alfabet, tanpa mengubah isi
print("\nUrutan alfabet (menggunakan sorted):")
print(sorted(places))

print("\nMenampilkan kembali urutan asli:")
print(places)

print("\nUrutan alfabet terbalik (menggunakan sorted):")
print(sorted(places, reverse=True))

print("\nMenampilkan kembali urutan asli:")
print(places)

#reverse() untuk mengubah urutan secara permanen
places.reverse()
print("\nSetelah reverse():")
print(places)

places.reverse()
print("\nSetelah reverse() kedua (kembali ke asli):")
print(places)

places.sort()
print("\nSetelah sort() (alfabet):")
print(places)

#sort(reverse=True) untuk mengubah menjadi alfabet terbalik
places.sort(reverse=True)
print("\nSetelah sort(reverse=True) (alfabet terbalik):")
print(places)