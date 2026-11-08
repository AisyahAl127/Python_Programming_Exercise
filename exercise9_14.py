from random import choice

#list berisi 10 angka dan 5 huruf
lottery_pool = (1, 3, 5, 7, 9, 12, 15, 22, 25, 42, 'a', 'b', 'c', 'd', 'e')

winning_ticket = []
while len(winning_ticket) < 4:
    selected = choice(lottery_pool)
    if selected not in winning_ticket:
        winning_ticket.append(selected)

print("--- Hasil Undian Lotere ---")
print(f"Kombinasi pemenang lotere adalah: {winning_ticket}")
print("Pesan: Tiket apa pun yang cocok dengan 4 angka atau huruf ini memenangkan hadiah!")