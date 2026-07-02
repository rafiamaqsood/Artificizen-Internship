# Write a function that accepts any number of arguments and returns their sum (use *args). 

def add(*num):
    total= 0
    for i in num:
        total+=i

    return total

print(add(1,2,3,4,5))