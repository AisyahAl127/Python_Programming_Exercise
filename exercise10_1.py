from pathlib import Path

path = Path('belajarpython.txt')

print("--- Membaca seluruh isi file sekaligus ---")
contents = path.read_text().rstrip()
print(contents)

print("\n--- Membaca dengan perulangan per baris ---")
lines = contents.splitlines()
for line in lines:
    print(line)