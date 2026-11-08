from random import randint

class Die:
    """Merepresentasikan sebuah dadu."""
    def __init__(self, sides=6):
        """Inisialisasi atribut sides dengan nilai default 6."""
        self.sides = sides

    def roll_die(self):
        """Mencetak angka acak antara 1 dan jumlah sisi dadu."""
        x = randint(1, self.sides)
        print(f"Hasil lemparan dadu {self.sides}-sisi: {x}")

# 1. Membuat dadu 6-sisi dan menggulingkannya 10 kali
print("--- Lemparan Dadu 6-Sisi ---")
d6 = Die()
for _ in range(10):
    d6.roll_die()

# 2. Membuat dadu 10-sisi dan menggulingkannya 10 kali
print("\n--- Lemparan Dadu 10-Sisi ---")
d10 = Die(10)
for _ in range(10):
    d10.roll_die()

# 3. Membuat dadu 20-sisi dan menggulingkannya 10 kali
print("\n--- Lemparan Dadu 20-Sisi ---")
d20 = Die(20)
for _ in range(10):
    d20.roll_die()