def talbum(nama, judul, nomer=None):
    """Membangun kamus yang berisi informasi tentang sebuah album musik."""
    album = {'artis': nama, 'judul album': judul}
    if nomer:
        album['songs'] = nomer
    return album

print("Masukkan informasi album (ketik 'q' untuk keluar kapan saja).")

while True:
    artis = input("Nama artis: ")
    if artis == 'q':
        break

    judul = input("Judul album: ")
    if judul == 'q':
        break

    album_dict = talbum(artis, judul)
    print(album_dict)