#Given a sentence, count the vowels and consonants separately. 

sentence = "it's a rainy day, we must took an umbrella with us"
vowels_count = 0
consonants_count = 0
vowels = ["a", "e", "i", "o", "u"]
for i in sentence.lower():
    if i.isalpha():
        if i in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
print(f"Vowels are {vowels_count} and Consonants are {consonants_count}")