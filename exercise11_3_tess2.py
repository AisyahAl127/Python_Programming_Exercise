import pytest
from exercise11_3_defff import karyawan

@pytest.fixture
def employee():
    """Sebuah fixture untuk membuat objek Employee yang dapat digunakan oleh tes."""
    return karyawan('budi', 'santoso', 50000)

def test_give_default_raise(employee):
    """Menguji apakah give_raise() dengan default $5,000 berfungsi dengan benar."""
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise(employee):
    """Menguji apakah give_raise() dengan jumlah kustom berfungsi dengan benar."""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000