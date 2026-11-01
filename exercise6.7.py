# Membuat dictionary untuk setiap orang
orang1 = {
    'first_name': 'Budi',
    'last_name': 'Santoso',
    'age': 20,
    'city': 'Jakarta'
}

orang2 = {
    'first_name': 'Siti',
    'last_name': 'Rahma',
    'age': 22,
    'city': 'Bandung'
}

orang3 = {
    'first_name': 'Eko',
    'last_name': 'Prasetyo',
    'age': 25,
    'city': 'Surabaya'
}

# Menyimpan dictionary ke dalam list bernama people
people = [orang1, orang2, orang3]

# Melakukan loop untuk mencetak informasi setiap orang
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nNama: {full_name}")
    print(f"Usia: {person['age']} tahun")
    print(f"Kota: {person['city']}")