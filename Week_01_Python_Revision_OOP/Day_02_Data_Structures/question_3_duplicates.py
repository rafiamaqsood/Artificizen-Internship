# Find duplicate elements in a list using a set.

number = [2,4,6,8,2,1,1]

seen = set()
duplicates = []
for i in number:
    if i in seen:
        duplicates.append(i)
    else:
        seen.add(i)
print(duplicates)
