def mobil(manufaktur, model, **info):
    """Menyimpan informasi tentang mobil dalam sebuah kamus."""
    info['manufaktur'] = manufaktur
    info['model'] = model
    return info

mobilku = mobil('subaru', 'outback', warna='blue')

print(mobilku)