from random import choice

def make_random_ticket(pool):
    """Membuat tiket acak berisi 4 elemen unik."""
    ticket = []
    while len(ticket) < 4:
        element = choice(pool)
        if element not in ticket:
            ticket.append(element)
    return ticket

def check_ticket(played_ticket, winning_ticket):
    """Memeriksa apakah semua elemen di played_ticket ada di winning_ticket."""
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True

# list lotere
lottery_pool = (1, 3, 5, 7, 9, 12, 15, 22, 25, 42, 'a', 'b', 'c', 'd', 'e')

# Tiket yang dimiliki
my_ticket = [7, 'b', 42, 15]

print(f"Tiket saya: {my_ticket}")
print("Sedang mencari tiket yang menang... Harap tunggu.")

count = 0
won = False

while not won:
    new_ticket = make_random_ticket(lottery_pool)
    count += 1
    if sorted(str(x) for x in new_ticket) == sorted(str(x) for x in my_ticket):
        won = True

print(f"Selesai! Perulangan harus berjalan sebanyak {count} kali untuk membuat tiket saya menang.")