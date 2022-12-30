pizzas = ['Jalapeno Pepperoni','Buffalo Chicken','BBQ Chicken']

friend_pizzas = pizzas[:]

pizzas.append('Meat Lovers')
friend_pizzas.append('Cheese')

print(f"My favorite pizzas are:\n")
for pizza in pizzas:
	print(pizza)
	
print(f"\nMy friend's favorite pizzas are: {friend_pizzas}\n")
for pizza in friend_pizzas:
	print(pizza)