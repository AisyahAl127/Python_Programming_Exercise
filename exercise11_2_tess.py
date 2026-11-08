from exercise11_2_defi import namakota

def test_namakota():
    """Menguji format kota dan negara tanpa populasi."""
    formatted_city = namakota('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'

def test_namakotapopulasi():
    """Menguji format kota, negara, dengan populasi."""
    formatted_city = namakota('santiago', 'chile', populasi=5000000)
    assert formatted_city == 'Santiago, Chile - populasi 5000000'