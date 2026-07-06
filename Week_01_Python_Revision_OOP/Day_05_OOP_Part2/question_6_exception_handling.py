# Write a try/except block that gracefully handles at least three different exception types (ValueError, ZeroDivisionError, FileNotFoundError).

try:
    num = int(input("Enter a number: "))
    result = 10 / num

    with open("sample.txt", "w") as file:
        file.write(str(result))
    with open("sample.txt","r") as file:
        print(file.read())


except ValueError:
    print("Error: Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except FileNotFoundError:
    print("Error: The file does not exist.")

else:
    print("Program executed successfully.")

finally:
    print("Program finished.")