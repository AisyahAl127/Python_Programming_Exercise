#1
prompt = "\nMasukkan topping pizza (ketik 'quit' untuk berhenti): "
topping = ""

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"Menambahkan {topping} ke pizza Anda!")
        
#2
prompt = "\nMasukkan topping pizza (ketik 'quit' untuk berhenti): "
aktif = True

while aktif:
    topping = input(prompt)
    if topping == 'quit':
        aktif = False
    else:
        print(f"Menambahkan {topping} ke pizza Anda!")
        

#3
prompt = "\nMasukkan topping pizza (ketik 'quit' untuk berhenti): "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Menambahkan {topping} ke pizza Anda!")