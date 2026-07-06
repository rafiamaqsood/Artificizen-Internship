# Write a program that reads a text file and reports the number of lines, words, and characters. 

with open("python_intro.txt", "r") as file:
    text=file.read()
    lines = len(text.splitlines())
    words= len(text.split())
    characters= len(text)

print(f"Number of lines are: {lines}")
print(f"Number of words are: {words}")
print(f"Number of characters are: {characters}")