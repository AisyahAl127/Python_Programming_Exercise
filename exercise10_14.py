from pathlib import Path
import json

def get_stored_username(path):
    """Ambil username yang tersimpan jika tersedia."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Meminta username baru."""
    username = input("Siapa nama Anda? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Menyapa pengguna berdasarkan namanya."""
    path = Path('username.json')
    username = get_stored_username(path)
    
    if username:
        konfirmasi = input(f"Apakah nama Anda {username}?: ")
        if konfirmasi.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
            return
            
    username = get_new_username(path)
    print(f"Kami akan mengingat Anda saat Anda kembali, {username}!")

greet_user()