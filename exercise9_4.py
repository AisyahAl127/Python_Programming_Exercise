#Menambahkan atribut number_served dari exercise 9.1

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi atribut nama restoran dan jenis masakan."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Mencetak ringkasan tentang restoran."""
        print(f"Nama restoran ini adalah {self.restaurant_name}.")
        print(f"Restoran ini menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        """Mencetak pesan yang menunjukkan restoran sedang buka."""
        print(f"{self.restaurant_name} sekarang buka!")

    def set_number_served(self, number):
        """Mengatur jumlah pelanggan yang telah dilayani ke nilai tertentu."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Menambahkan jumlah pelanggan yang dilayani berdasarkan angka tertentu."""
        self.number_served += additional_customers

restaurant = Restaurant('The Italian Place', 'Italia')

print(f"Jumlah pelanggan yang dilayani: {restaurant.number_served}")

restaurant.number_served = 15
print(f"Jumlah pelanggan setelah diubah langsung: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Jumlah pelanggan setelah menggunakan set_number_served(): {restaurant.number_served}")

restaurant.increment_number_served(35)
print(f"Jumlah pelanggan setelah di-increment: {restaurant.number_served}")