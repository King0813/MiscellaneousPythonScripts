change_name = ()

new_name = ""
new_pin = 0
new_password = ""

class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self,name):
        self.name = name 
        #print("Your name has been changed to: ", self.name)

    def change_pin(self,pin):
        self.pin = pin 
        #print("Your pin has been changed to: ", self.pin)

    def change_password(self,password):
        self.password = password 
        #print("Your password has been changed to: ", self.password)





customer = User("Bob", 1200, "job")
print(customer.name, customer.pin, customer.password)

customer.change_name("Bobby")
customer.change_pin(4321)
customer.change_password("newpassword")
print(customer.name, customer.pin, customer.password)
 

# class Stack:
#     def __init__(self):
#         self.head = None
#         self.num_nodes = 0

#     def push(self, value):
#         new_node = Node(value)

#         if self.head is not None:
#             new_node.next = self.head

#         self.head = new_node
#         self.num_nodes += 1

#     def pop(self):
#         if self.head == None:
#             return None
        
#         pop_node = self.head.value
#         self.head = self.head.next
#         self.num_nodes += 1
#         return pop_node

# stack = Stack()
# stack.push(1)   
# stack.push(2)   
# stack.push(3)   
# stack.push(4)

# print("Pass" if (stack.num_nodes == 5) else "Fail")
# stack.push(5)
# print("Pass" if (stack.num_nodes == 5) else "Fail")

# print("Pass" if (stack.pop() == 5) else "Fail")
# print("Pass" if (stack.pop() == 4) else "Fail")