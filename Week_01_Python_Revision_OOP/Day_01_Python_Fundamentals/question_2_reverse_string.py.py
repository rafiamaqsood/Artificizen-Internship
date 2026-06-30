#Reverse a string without using slicing or a built-in reverse function.

string = input("Enter string: ")
reverse = ""
for i in string:
    reverse  = i + reverse

print(reverse)