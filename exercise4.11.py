pizzas = ['pepperoni', 'hawaiian', 'meat lovers']

temanpizza = pizzas[:] #daftar dengan irisan

pizzas.append('bbq chicken')
temanpizza.append('veggie')

print("Pizza kesukaan saya adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza kesukaan teman saya adalah:")
for pizza in temanpizza:
    print(pizza)