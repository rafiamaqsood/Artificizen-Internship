# Write a function that returns the most frequent element in a list.

number = [2,4,6,8,10,12,2,4]

def freq_element(num):
    frequency = {}
    for i in num:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return max(frequency, key=frequency.get)
print(freq_element(number))