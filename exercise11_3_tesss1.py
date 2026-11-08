from exercise11_3_defff import karyawan

def test_give_default_raise():
    """Menguji apakah give_raise() dengan default $5,000 berfungsi dengan benar."""
    employ = karyawan('budi', 'santoso', 50000)
    employ.give_raise()
    assert employ.annual_salary == 55000

def test_give_custom_raise():
    """Menguji apakah give_raise() dengan jumlah kustom berfungsi dengan benar."""
    employ = karyawan('budi', 'santoso', 50000)
    employ.give_raise(10000)
    assert employ.annual_salary == 60000