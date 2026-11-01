def deskkota(kota, negara='Islandia'):
    """Menampilkan kalimat yang mendeskripsikan suatu kota dan negaranya."""
    print(f"{kota} berada di {negara}.")

deskkota('Reykjavik')                  # Menggunakan negara default
deskkota('Paris', 'Prancis')           # Menggunakan negara non-default
deskkota('Tokyo', 'Jepang')