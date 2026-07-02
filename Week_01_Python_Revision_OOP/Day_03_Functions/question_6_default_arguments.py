# Write a function with a default argument, and add a comment explaining why mutable default arguments (like a list) are risky in Python. 

def info(name, age=20):
    print(name, age)

info("Rafia")
info("Sawera",32)

''' Why are mutable default arguments risky?
 Mutable objects (like lists or dictionaries) are created only once
 when the function is defined, not every time it is called.
 As a result, all function calls share the same object, which can
 lead to unexpected behavior.

 Example (Bad):
 def add_item(item, my_list=[]):
     my_list.append(item)
     return my_list
 print(add_item(1))  # [1]
 print(add_item(2))  # [1, 2]  <- Same list is reused!
 print(add_item(3))  # [1, 2, 3]
 Instead, use None and create a new list inside the function:
 def add_item(item, my_list=None):
     if my_list is None:
         my_list = []
     my_list.append(item)
     return my_list 
'''
