class User:
    def __init__(self, first_name, last_name, username, email, location):
        """Inisialisasi atribut profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        """Mencetak ringkasan informasi pengguna."""
        print(f"\nProfil Pengguna: {self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Lokasi: {self.location}")

    def greet_user(self):
        """Mencetak sapaan yang dipersonalisasi untuk pengguna."""
        print(f"Halo, {self.first_name} {self.last_name} ({self.username})! Selamat datang kembali.")

# Membuat instance dan memanggil metode
user1 = User('Lana', 'Lovelace', 'alovelace', 'lanaa@example.com', 'Boyolali')
user2 = User('Lina', 'Turing', 'aturing', 'Lin4a@example.com', 'Sukoharjo')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()