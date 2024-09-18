products = []
while True:
	name = input('please input merchandise name: ')
	if name == 'q':
		break
	price = input('please input merchandise price: ')
	# p = []		# small list
	# p.append(name)
	# p.append(price)
	p = [name, price]	# replace rows 7~9
	# products.append(p)	# big list, p is included in products
	products.append([name, price]) # omit p list
print(products)
print(products[0][0])
print(products[1][1])
print(products[2][1])
for p in products:
	print(p)
	print(p[0], 'unit price is', p[1])