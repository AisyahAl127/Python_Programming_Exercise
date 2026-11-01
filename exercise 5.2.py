# 1. Tes Kesamaan dan Ketidaksamaan dengan String 
bahasa = 'Python'
print("--- Tes String ---")
print(bahasa == 'Python')  # True
print(bahasa == 'Java')    # False

#2. Tes Menggunakan Metode lower()
teks = 'Belajar PYTHON'
print("\n--- Tes Metode lower() ---")
print(teks.lower() == 'belajar python')  # True
print(teks.lower() == 'belajar java')    # False

#3. Tes Numerik (Kesamaan, Ketidaksamaan, Lebih/Kurang Dari)
angka = 25
print("\n--- Tes Numerik ---")
print(angka == 25)    # True (Kesamaan)
print(angka != 30)    # True (Ketidaksamaan)
print(angka > 20)     # True (Lebih besar dari)
print(angka < 10)     # False (Kurang dari)
print(angka >= 25)    # True (Lebih besar atau sama dengan)
print(angka <= 20)    # False (Kurang atau sama dengan)

#4. Tes Menggunakan Keyword 'and' dan 'or'
nilai_matematika = 85
nilai_fisika = 90
print("\n--- Tes 'and' dan 'or' ---")
# 'and' jika keduanya benar
print(nilai_matematika >= 80 and nilai_fisika >= 80)  # True
print(nilai_matematika >= 90 and nilai_fisika >= 80)  # False

# 'or' jika salah satu atau keduanya benar
print(nilai_matematika >= 90 or nilai_fisika >= 80)   # True
print(nilai_matematika < 80 or nilai_fisika < 80)     # False

#5. Pembuktian item ada di dalam list ('in')
hewan = ['kucing', 'kelinci', 'hamster']
print("\n--- Tes 'in' ---")
print('kelinci' in hewan)  # True
print('burung' in hewan)   # False

#6. Pembuktian item tidak di dalam list ('not in')
print("\n--- Tes 'not in' ---")
print('ular' not in hewan)    # True
print('kucing' not in hewan)  # False