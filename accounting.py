products = []
# used input data
while True:
	name = input('please input merchandise name: ')
	if name == 'q':
		break
	price = input('please input merchandise price: ')
	price = int(price)	# convert prince to integer
	# p = []		# small list
	# p.append(name)
	# p.append(price)
	p = [name,price]	# replace rows 7~9
	# products.append(p)	# big list, p is included in products
	products.append([name,price]) # omit p list
print(products)
print(products[0][0])
print(products[1][1])
print(products[2][1])

# print pruchase record
for p in products:
	# print(p)
	print(p[0], 'unit price is', p[1])

# write into file
# with open('product.txt', 'w') as f:
with open('product.csv', 'w', encoding = 'utf-8') as f:	# change .txt to .csv, use utf-8 encoding to avoid garbled code(亂碼)
	f.write('merchandise,price\n')	# add title on first row
	for p in products:
		# f.write(p[0] + ',' + p[1] + '\n'), ',' is a delimiter
		# + 只能用來合併字串跟字串或整數跟整數
		f.write(p[0] + ',' + str(p[1]) + '\n')	# 因price已被宣告成整數, 故與p[0]合併前需先轉換為字
# use Excel to import csv file: data->get external data->from txt file->file origin:'UTF-8'->delimiters:'comma'

# read file
with open('product.csv', 'r', encoding = 'utf-8') as f:	# encoding must be consistent on rows 3 and 29 
	for line in f:
		if 'merchandise,price' in line:
			continue # jump to next loop, for hiding 'merchandise,price'
		name, price = line.strip().split(',')	# strip(): remove \n(換行), split(','): 用逗點做分割
		# split後的結果會是清單, 所以 s = list
		products.append([name, price])
print(products)