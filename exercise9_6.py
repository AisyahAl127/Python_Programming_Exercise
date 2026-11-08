from exercise9_1 import Restaurant

class IceCreamStand(Restaurant):
    """Merepresentasikan stan es krim, jenis khusus dari restoran."""
    def __init__(self, restaurant_name, cuisine_type='es krim'):
        """Inisialisasi atribut dari kelas induk, lalu atribut khusus es krim."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Vanila', 'Cokelat', 'Stroberi', 'Matcha']

    def display_flavors(self):
        """Menampilkan daftar rasa es krim yang tersedia."""
        print(f"Daftar rasa es krim di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Membuat instance dari IceCreamStand dan memanggil metode
my_ice_cream_stand = IceCreamStand('Sweet Scoop')
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.display_flavors()