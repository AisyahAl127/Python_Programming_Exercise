sungai = {
    'nil': 'mesir',
    'amazon': 'brazil',
    'han': 'korea'
}

# 1. kalimat tentang setiap sungai
print("--- Informasi Sungai ---")
for river, country in sungai.items():
    print(f"Sungai {river.capitalize()} mengalir melalui {country.capitalize()}.")

#2. nama sungai menggunakan loop
print("\n--- Daftar Sungai ---")
for river in sungai.keys():
    print(river.capitalize())

#3. nama negara menggunakan loop
print("\n--- Daftar Negara ---")
for country in sungai.values():
    print(country.capitalize())