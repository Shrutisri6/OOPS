from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def update_price(self, amount):
        if amount >= 0:
            self.__price = amount


class User:
    def __init__(self, name):
        self.name = name


class Customer(User):
    def order(self):
        return Order()

    def pay(self, order, payment):
        order.process_payment(payment)


class Admin(User):
    def change_price(self, product, new_price):
        product.update_price(new_price)


class Payment(ABC):
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print("Paid using Card")


class UpiPayment(Payment):
    def pay(self, amount):
        print("Paid using UPI")


class WalletPayment(Payment):
    def pay(self, amount):
        print("Paid using Wallet")


class Order:
    def __init__(self):
        self.products = []
        self.discount = 0

    def add_product(self, product):
        self.products.append(product)

    def apply_discount(self, percent):
        self.discount = percent

    def total(self):
        total = sum(p.get_price() for p in self.products)
        return total - self.discount
    def process_payment(self, payment):
        payment.pay(self.total())


admin = Admin("Admin")
customer = Customer("Alice")

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)

admin.change_price(p2, 900)

order = customer.order()
order.add_product(p1)
order.add_product(p2)
order.apply_discount(10)

print("Total:", order.total())

customer.pay(order, CardPayment())
customer.pay(order, UpiPayment())
customer.pay(order, WalletPayment())
