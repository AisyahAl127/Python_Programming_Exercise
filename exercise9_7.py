from exercise9_3 import User

class Admin(User):
    """Merepresentasikan pengguna khusus dengan hak istimewa administrator."""
    def __init__(self, first_name, last_name, username, email, location):
        """Inisialisasi atribut dari kelas induk, lalu atribut privileges."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = ["bisa menambah postingan", "bisa menghapus postingan", "bisa melarang pengguna (ban)"]

    def show_privileges(self):
        """Menampilkan daftar hak istimewa administrator."""
        print(f"Hak istimewa untuk Admin {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Membuat instance dari Admin dan memanggil metode
admin_user = Admin('Siti', 'Aminah', 'siti_admin', 'siti@example.com', 'Bandung')
admin_user.describe_user()
admin_user.show_privileges()