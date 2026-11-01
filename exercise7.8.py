sandwichorders = ['tuna', 'ayam', 'keju', 'turki', 'roast beef','pastrami']
finished_sandwiches = []

while sandwichorders:
    pesanan = sandwichorders.pop()
    print(f"Saya membuat sandwich {pesanan} Anda.")
    finished_sandwiches.append(pesanan)

print("\nBerikut adalah sandwich yang telah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")