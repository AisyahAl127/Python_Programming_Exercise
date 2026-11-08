class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut nama restoran dan jenis masakan."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Mencetak ringkasan tentang restoran."""
        print(f"Nama restoran ini adalah {self.restaurant_name}.")
        print(f"Restoran ini menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        """Mencetak pesan yang menunjukkan restoran sedang buka."""
        print(f"{self.restaurant_name} sekarang buka!")

restaurant = Restaurant('Ayam Goreng Pak Cik', 'Makanan Padang')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()