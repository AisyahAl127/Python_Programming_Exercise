# Membuat dictionary untuk setiap hewan peliharaan
pet_1 = {'hewan': 'kucing', 'pemilik': 'budi'}
pet_2 = {'hewan': 'anjing', 'pemilik': 'siti'}
pet_3 = {'hewan': 'burung', 'pemilik': 'eko'}
pet_4 = {'hewan': 'hamster', 'pemilik': 'dewi'}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"\nJenis Hewan: {pet['hewan'].capitalize()}")
    print(f"Nama Pemilik: {pet['pemilik'].capitalize()}")