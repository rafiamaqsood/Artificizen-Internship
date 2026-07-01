# Use a list comprehension to extract all even numbers from a list in one line. 

numbers = [12, 7, 9, 20, 4, 15]
even_numbers=[i for i in numbers if i%2==0]
print(even_numbers)