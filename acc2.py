import os # loading operating system

products = []

if os.path.isfile('products.csv'): # check if csv file exists
	print('file found')
	# read from csv
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'merchandise,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('file not found')

# user input
while True:
	name = input('please input merchandise: ')
	if name == 'q':
		break
	price = input('please input unit price: ')
	price = int(price)
	products.append([name, price])
print(products)

# print purchase record
for p in products:
	print('the price of', p[0], 'is', p[1])

# write into csv
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('merchandise,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')