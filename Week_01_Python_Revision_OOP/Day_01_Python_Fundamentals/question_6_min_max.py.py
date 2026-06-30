# Given a list of numbers, find the largest and smallest without using min()/max().
num = [5,10,100,30,2]
max = num[0]
min = num[0]
for i in num:
    if i > max:
        max = i
    if i < min:
        min = i
print(f"Largest number is {max}")
print(f"Smallest number is {min}")
print(max(num))