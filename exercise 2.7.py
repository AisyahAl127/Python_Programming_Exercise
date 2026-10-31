#Menyimpan variabel dengan karakter whitespace di awal dan akhir (\t dan \n)
name = "\t\n  Albert Einstein  \n\t"

print("Nama asli dengan whitespace:")
print(name)

#fungsi lstrip()
print("\nMenggunakan lstrip():")
print(name.lstrip())

#fungsi rstrip()
print("\nMenggunakan rstrip():")
print(name.rstrip())

#fungsi strip()
print("\nMenggunakan strip():")
print(name.strip())