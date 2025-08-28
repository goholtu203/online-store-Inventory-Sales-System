store_dict = {}
def start():
	while True:
		print("""
		Select an option:
		1. Add product
		2. Update Stock
		3. Sell Prodcut
		4. Display Inventory
		5. Most Expensive product
		6. Total potential Sales
		0. exit
		""")
		user_option = int(input("Option:>>>"))
		if user_option == 1:
			name = input("Name of product: >>>").upper().strip()
			price = float(input("Price: >>>"))
			quantity = int(input("Quantity: >>>"))
			add_product(store_dict, name, price, quantity)

		elif user_option == 2:
			name = input("Enter product name:>>>").upper().strip()
			quantity = int(input("Qantity:>>>"))
			update_stock(store_dict, name, quantity)
		elif user_option == 3:
			name = input("Enter prodcut name:>>>").upper().strip()
			quantity = int(input("Quantity: >>"))
			print("The total sell price is:", sell_product(store_dict, name, quantity))
		elif user_option == 4:
			print("The total number of products in store is:", display_inventory(store_dict))
		elif user_option == 5:
			print(f"The most expensive product is:{ most_expensive_product(store_dict)}")
		elif user_option == 6:
			print(f"The total potential sale of product left is:{total_potential_sales(store_dict):,.2f}₦")
		elif user_option == 0:
			break
		else:
			print("Invalid Option")


def add_product(store_dict, name, price, quantity):
    if name not in store_dict:
        record = {"price": price, "quantity": quantity}
        store_dict[name] = record
        print(f"{name} successfully added to store")
    else:
        print("Product already exists")
    print(store_dict)

#Update the stock of an existing product.
#Return a success message if updated, or an error message if the product does not exist.


def update_stock(store_dict, name, quantity):
    if name not in store_dict:
        print("Product does not exist")
    else:
        store_dict[name]["quantity"] += quantity
        print(f"Successfully updated the stock of {name}")
    print(store_dict)
#Process a sale for the given product and quantity.
#If enough stock exists, reduce the quantity and return the total sale price.
#If stock is insufficient or product does not exist, return an appropriate error message.


def sell_product(store_dict, name, quantity):
    if name not in store_dict:
        print("Oops!! Product not in store.")
    elif store_dict[name]["quantity"] < quantity:
        print(f"Not enough to supply... You requested {quantity} but only {store_dict[name]['quantity']} is available")
    else:
        store_dict[name]["quantity"] -= quantity
        print(f"Sold {quantity} of {name}")
        total_sale_price = store_dict[name]['price'] * quantity
    return total_sale_price
       


#Print all products with their prices and remaining quantity.
#Return the total number of products displayed.


def display_inventory(store_dict):
    serial_no = 1
    for products, values in store_dict.items():
	    product = products
	    price = values["price"]
	    quantity= values["quantity"]
	    inventory = f"{serial_no}-- Product Name: {product}, Price: {price}, Quantity in store: {quantity}"
	    print(inventory)
	    serial_no += 1
    return len(store_dict)

#Find and return the product with the highest price along with its price.


def most_expensive_product(store_dict):
	price= 0
	product = None
	for products, values in store_dict.items():
		if values['price'] > price:
			price = f"Price: {values['price']:,.2f}₦"
			product = products
	return product, price
#Calculate the total value of all remaining stock  and return it.


def total_potential_sales(store_dict):
	potential_sale = 0
	for values in store_dict.values():
		potential_sale += values['price']*values['quantity']
	return potential_sale

start()

