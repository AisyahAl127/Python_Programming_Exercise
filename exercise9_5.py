#Menambahkan atribut self.login_attemps dari exercise 9.3

class User:
    def __init__(self, first_name, last_name, username, email, location):
        """Inisialisasi atribut profil pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Mencetak ringkasan informasi pengguna."""
        print(f"\nProfil Pengguna: {self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Lokasi: {self.location}")

    def greet_user(self):
        """Mencetak sapaan yang dipersonalisasi untuk pengguna."""
        print(f"Halo, {self.first_name} {self.last_name} ({self.username})! Selamat datang kembali.")

    def increment_login_attempts(self):
        """Menaikkan nilai login_attempts sebesar 1[cite: 11]."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mengatur ulang nilai login_attempts menjadi 0[cite: 11]."""
        self.login_attempts = 0

user1 = User('Budi', 'Santoso', 'bsantoso', 'budi@example.com', 'Jakarta')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Jumlah percobaan login: {user1.login_attempts}")

user1.reset_login_attempts()

print(f"Jumlah percobaan login setelah terreset: {user1.login_attempts}")