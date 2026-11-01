tempatsuka = {
    'andi': ['pantai', 'gunung'],
    'siti': ['perpustakaan', 'alun-alun', 'taman kota'],
    'eko': ['museum']
}

# Melakukan loop melalui dictionary
for nama, tempat in tempatsuka.items():
    print(f"\nTempat-tempat favorit {nama.capitalize()} adalah:")
    for place in tempat:
        print(f"\t- {place.capitalize()}")