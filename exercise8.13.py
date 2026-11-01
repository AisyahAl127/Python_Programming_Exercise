def profil(ndepan, nbel, **info):
    """Membangun kamus yang berisi segala hal yang kita ketahui tentang pengguna."""
    info['nama depan'] = ndepan
    info['nama belakang'] = nbel
    return info

profilku = profil(
    'aisyah', 
    'al',
    lokasi='solo',
    gedung='teknink industi',
    hobi='membaca buku'
)

print ("inilah profilku")
print (profilku)
