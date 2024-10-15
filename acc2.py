import os # loading operating system
products = []

# read from csv (function中應只涵蓋單一功能)
def read_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if 'merchandise,price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# user input
def user_input(products): 
    while True:
        name = input('please input merchandise: ')
        if name == 'q':
            break
        price = input('please input unit price: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

# print purchase record
def print_products(products):
    for p in products:
        print('the price of', p[0], 'is', p[1])

# write into csv
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('merchandise,price\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): # check if csv file exists
        print('file found')
        products = read_file(filename)
    else:
        print('file not found')
    products = user_input(products)
    print_products(products)
    products = write_file(filename, products)

main()
# refactor (重構)
