# Write a program to check whether a number is prime.

is_prime = True
number = int(input("Enter number: "))
if (number<=1):
    is_prime= False
else:
    for i in range(2,number):
        if (number%i == 0):
          is_prime = False

          break
if (is_prime):
     print (f"Number {number} is prime") 
else:
    print (f"Number {number} is not prime")
        
 
        
    
    
