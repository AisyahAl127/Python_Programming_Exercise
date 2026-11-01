bahasafav = {
    'jena': 'python',
    'sarah': 'c',
    'doni': 'rust',
    'rudi': 'python',
}

# Daftar orang yang harus/akan diajak mengikuti poll
poll = ['jena', 'budi', 'edward', 'siti', 'sarah', 'eko','rudi']

# Melakukan loop untuk mengecek status poll setiap orang
for person in poll:
    if person in bahasafav.keys():
        print(f"Terima kasih, {person.title()}, karena telah meluangkan waktu untuk merespons poll ini!")
    else:
        print(f"Halo {person.title()}, Anda diundang untuk mengikuti poll bahasa pemrograman favorit kami!")