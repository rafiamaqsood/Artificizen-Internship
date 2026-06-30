# Check if a given string is a palindrome.
string = input("Enter string: ").lower()
reverse = ""
for i in string:
    reverse  = i + reverse

if (string == reverse):
    print("Palindrome")
else:
    print("Not Palindrome")