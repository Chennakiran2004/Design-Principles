from abc import ABC, abstractmethod

# <------------ Single Responsibility ------------>
class Order:
    def __init__(self, food_name, price):
        self.food_name = food_name
        self.price = price
        
    def display_order(self):
        print(f"Food: {self.food_name}")
        print(f"Price: {self.price}")
        
class PaymentService:
    def process_payment(self, amount):
        print(f"Processing Payment of {amount}")
        
class OrderRepository:
    def save_to_database(self, order):
        print(f"Order {order.food_name} saved to database")
    
class EmailService:
    def send_confirmation_mail(self, order):
        print(f"Confirmation email sent for {order.food_name}")
        
        
# <------------ Open/Closed Principle ------------>
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass 

class UPIPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying {amount} using UPI")
        
class CardPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying {amount} using Card")

class WalletPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paying {amount} using Wallet amount")


# <------------ Liskov Substitution Principle ------------>
def checkout(payment_processor, amount):
    payment_processor.pay(amount)
    

checkout(UPIPayment(), 250)
checkout(CardPayment(), 250)
checkout(WalletPayment(), 250)
   
# <------------ Interface Segregation Principle ------------> 

class Refundable(ABC):
    @abstractmethod
    def refund(self, amount):
        pass

class InstallmentPayment(ABC):
    @abstractmethod
    def pay_in_installement(self, amount):
        pass

class UPIPayment1(PaymentProcessor, Refundable):
    def pay(self, amount):
        print(f"Paying ₹{amount} using UPI")

    def refund(self, amount):
        print(f"Refunding ₹{amount} through UPI")

class CardPayment1(PaymentProcessor, Refundable, InstallmentPayment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using Card")

    def refund(self, amount):
        print(f"Refunding ₹{amount} to Card")

    def pay_in_installments(self, amount):
        print(f"Paying ₹{amount} in installments")
        
# <------------ Dependency Inversion Principle ------------> 
class OrderService:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor
        
    def checkout(self, amount):
        self.payment_processor.pay(amount)


upi_order_service = OrderService(UPIPayment())
upi_order_service.checkout(250)

card_order_service = OrderService(CardPayment())
card_order_service.checkout(500)

# order = Order("Pizza", 250)
# order.dispaly_order()

# order = Order("Pizza", 250)

# order.display_order()

# payment = PaymentService()
# payment.process_payment(order.price)

# repository = OrderRepository()
# repository.save_to_database(order)

# email = EmailService()
# email.send_confirmation_mail(order)

# upi = UPIPayment()
# upi.pay(250)

# card = CardPayment()
# card.pay(250)

# wallet = WalletPayment()
# wallet.pay(250)

# checkout(UPIPayment(), 250)
# checkout(CardPayment(), 250)
# checkout(WalletPayment(), 250)