def album(artis, judul, jumlah=None):
    """Membangun kamus yang berisi informasi tentang sebuah album musik."""
    album = {'artis': artis, 'judul': judul}
    if jumlah:
        album['songs'] = jumlah
    return album

album1 = album('Adele', '25')
album2 = album('Ed Sheeran', 'Divide')
album3 = album('Taylor Swift', '1989', jumlah=16)

print(album1)
print(album2)
print(album3)