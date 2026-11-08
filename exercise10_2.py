from pathlib import Path

# Tentukan path file
path = Path('belajarpython.txt')
contents = path.read_text()
lines = contents.splitlines()

# Membaca setiap baris dan mengganti kata 'Python' dengan 'C'
print("--- Modifikasi teks Python menjadi C ---")
for line in lines:
    modified_line = line.replace('Python', 'C')
    print(modified_line)