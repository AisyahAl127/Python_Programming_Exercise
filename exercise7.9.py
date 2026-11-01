sandwich_orders = ['tuna','pastrami', 'ayam', 'keju', 'turki', 'roast beef','pastrami']
finished_sandwiches = []

print("Maaf, deli sedang kehabisan pastrami hari ini.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"Saya membuat sandwich {current_order} Anda.")
    finished_sandwiches.append(current_order)

print("\nBerikut adalah sandwich yang telah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- Sandwich {sandwich}")