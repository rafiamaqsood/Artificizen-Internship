# Count the frequency of each word in a sentence using a dictionary.

sentence= input("Write a sentence: ").lower()
words= sentence.split()
dic={
    i:words.count(i)
    for i in words
}
print (dic)