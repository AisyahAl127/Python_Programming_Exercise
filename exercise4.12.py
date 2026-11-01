foods = ['ubi', 'roti bakar', 'molen']
temanfoods = foods[:]

foods.append('martabak')
temanfoods.append('batagor')

print("Makanan kesukaan saya adalah:")
for food in foods:
    print(food)

print("\nMakanan kesukaan teman saya adalah:")
for food in temanfoods:
    print(food)