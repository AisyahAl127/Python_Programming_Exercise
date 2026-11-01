rivers = ['bengawan', 'bogowonto', 'ciliwung', 'mississippi', 'han']

#1. len() untuk menghitung panjang daftar
print(f"Jumlah sungai dalam daftar awal: {len(rivers)}")

#2. append() untuk menambah item di akhir
rivers.append('mahakam')

#3. insert() untuk menambah item di posisi (x, 'item')
rivers.insert(0, 'musi')

#4. del untuk menghapus item berdasarkan indeks
del rivers[1]

#5. pop() untuk menghapus item terakhir dan menggunakannya
popped_river = rivers.pop()
print(f"Sungai yang dihapus dengan pop: {popped_river}")

#6. remove() untuk menghapus item berdasarkan nilai
rivers.remove('han')

#7. sorted() untuk menampilkan daftar secara alfabetis (sementara)
print("\nDaftar berurutan sementara (sorted):")
print(sorted(rivers))

#8. daftar asli tidak berubah
print("\nDaftar asli tetap tidak berubah:")
print(rivers)

#9. reverse() untuk membalikkan urutan secara permanen
rivers.reverse()
print("\nDaftar setelah dibalik (reverse):")
print(rivers)

#10. sort() untuk mengurutkan secara permanen (alfabetis)
rivers.sort()
print("\nDaftar setelah diurutkan permanen (sort):")
print(rivers)