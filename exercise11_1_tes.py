from exercise11_1_def import namakota

def test_namakota():
    """Apakah kota dan negara seperti 'santiago, chile' bekerja dengan benar?"""
    samed_city = namakota('santiago', 'chile')
    assert samed_city == 'Santiago, Chile'
    