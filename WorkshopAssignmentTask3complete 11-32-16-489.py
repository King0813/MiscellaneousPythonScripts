change_name = ()
 
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self,name):
        self.name = name 
         
    def change_pin(self,pin):
        self.pin = pin 
         
    def change_password(self,password):
        self.password = password 

class BankUser(User):
    def __init__(self, name, pin, password):
        balance = 0
        super().__init__(name, pin, password, balance)
        self.balance = 0
         




customer = User("Bob", 1200, "job")
print(customer.name, customer.pin, customer.password)

customer.change_name("Bobby")
customer.change_pin(4321)
customer.change_password("newpassword")
print(customer.name, customer.pin, customer.password)
 
 