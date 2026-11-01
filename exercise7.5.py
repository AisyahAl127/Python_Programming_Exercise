prompt = "Berapa usia Anda?\n"
prompt += "(Ketik 'quit' untuk keluar) \n Umur anda: "

while True:
    age_input = input(prompt)
    
    if age_input == 'quit':
        break
        
    age = int(age_input)
    
    if age < 3:
        print("Tiket Anda gratis!")
    elif age <= 12:
        print("Harga tiket Anda adalah 30.000 rupiah.")
    else:
        print("Harga tiket Anda adalah 50.000 rupiah.")
