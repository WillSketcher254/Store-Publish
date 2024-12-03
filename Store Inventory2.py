present_stock = {
    'lotion': 32,
    'shoes': 22,
    'mattress': 12
}

vip_members = ['Steve Jobs', 'Mark Williams', 'Zetech Guy', 'Princess Fiona']

#Main Class Product
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            present_stock[self.name] = self.stock
            return True
        else:
            print(f"Not enough stock for {self.name}. Available: {self.stock}")
            return False

    def restock(self, quantity):
        self.stock += quantity
        present_stock[self.name] = self.stock
        print(f"{self.name} restocked. New quantity: {self.stock}")

    def __str__(self):
        return f"Product(Name: {self.name}, Price: {self.price}, Stock: {self.stock})"


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchase_history = []

    def add_order(self, order):
        self.purchase_history.append(order)

    def total_spent(self):
        return sum(order.total_price() for order in self.purchase_history)

    def __str__(self):
        return f"Customer(Name: {self.name}, Email: {self.email}, Purchases: {len(self.purchase_history)})"


class VipCustomer(Customer):
    discount_rate = 0.8

    def apply_discount(self, total_price):
        return total_price * self.discount_rate


class Order:
    def __init__(self, product, quantity, customer):
        self.product = product
        self.quantity = quantity
        self.customer = customer

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"Order(Customer: {self.customer.name}, Product: {self.product.name}, Quantity: {self.quantity}, Total: {self.total_price()})"


def order_inputs():
    customer_name = input("Enter your name: ").strip()
    customer_email = input("Enter your email: ").strip()
    product_name = input("Enter the product name: ").lower().strip()
    quantity = int(input("Enter the quantity to purchase: "))

    if product_name not in present_stock:
        print("Sorry, the product is not available.")
        return

    product_stock = present_stock[product_name]
    if quantity > product_stock:
        print(f"Sorry, we only have {product_stock} available.")
        return

    product_price = float(input("Enter the product price: "))
    product = Product(product_name, product_price, product_stock)

    if customer_name in vip_members:
        customer = VipCustomer(customer_name, customer_email)
        total = product_price * quantity
        discounted_total = customer.apply_discount(total)
        print(f"VIP Discount Applied. You pay: {discounted_total}")
    else:
        customer = Customer(customer_name, customer_email)

    if product.sell(quantity):
        order = Order(product, quantity, customer)
        customer.add_order(order)
        print(order)
    else:
        print("Order could not be completed due to insufficient stock.")


def restocking():
    product_name = input("Enter the product name to restock: ").lower().strip()
    quantity = int(input("Enter the restock quantity: "))

    if product_name in present_stock:
        product = Product(product_name, 0, present_stock[product_name])
        product.restock(quantity)
    else:
        price = float(input("Enter the price of the new product: "))
        new_product = Product(product_name, price, quantity)
        present_stock[product_name] = quantity
        print(f"New product added: {new_product}")


def main():
    print('For customer service write "cs", \nFor restocking write "rs", \nTo view current stock write "st", \nTo quit write "q".')
    while True:
        user = input("\nEnter command (cs, rs, st, q): ").lower()
        if user == 'cs':
            order_inputs()
        elif user == 'rs':
            restocking()
        elif user == 'st':
            for name, stock in present_stock.items():
                print(f"Product: {name}, Stock: {stock}")
        elif user == 'q':
            break
        else:
            print("Invalid command. Try again.")

main()