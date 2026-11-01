prompt = "Masukkan topping pizza yang ingin Anda tambahkan!\n" 
prompt += "(Ketik 'quit' jika sudah selesai) \n topping: "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f"Kami akan menambahkan {topping} ke pizza Anda!")