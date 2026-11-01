angkasuka = {
    'andi': [7, 14, 21],
    'siti': [12, 30],
    'eko': [3, 9, 27, 81],
    'dewi': [5],
    'rizki': [21, 99]
}

for nama, angka in angkasuka.items():
    print(f"\nNomor favorit {nama.capitalize()} adalah:")
    for number in angka:
        print(f"\t{number}")