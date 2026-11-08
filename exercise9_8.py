from exercise9_3 import User

class Privileges:
    """Kelas terpisah untuk menyimpan dan mengelola daftar hak istimewa."""
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["bisa menambah postingan", "bisa menghapus postingan", "bisa melarang pengguna (ban)"]
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak istimewa."""
        print("Daftar Hak Istimewa:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Merepresentasikan pengguna dengan hak istimewa menggunakan komposisi."""
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        # Membuat instance Privileges sebagai atribut
        self.privileges = Privileges()

# Membuat instance Admin baru dan memanggil metode melalui atribut privileges
admin_user_2 = Admin('Jaka', 'Tamin', 'j4ka_t', 'jakt@example.com', 'Solo')
admin_user_2.describe_user()
admin_user_2.privileges.show_privileges()