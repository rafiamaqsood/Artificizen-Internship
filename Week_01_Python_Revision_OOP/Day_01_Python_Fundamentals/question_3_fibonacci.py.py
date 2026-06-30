#Print the Fibonacci series up to n terms.
num = int(input("Enter number: "))
num1= 0
num2=1
if num == 1:
    print(0)

elif num >= 2:
    print(num1, num2, sep="\n")
    for i in range(num-2):
        num3 = num1 + num2
        num1=num2
        num2=num3
        print(num3)
    

