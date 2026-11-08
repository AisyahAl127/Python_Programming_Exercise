def namakota(kota, negara, populasi=''):
    """Mengembalikan string format Kota, Negara - populasi xxx."""
    if populasi:
        output = f"{kota.title()}, {negara.title()} - populasi {populasi}"
    else:
        output = f"{kota.title()}, {negara.title()}"
    return output
