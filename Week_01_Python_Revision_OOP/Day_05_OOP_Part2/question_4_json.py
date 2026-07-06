#Write a program that saves a list of dictionaries (student records) to a JSON file, then loads them back. 

import json
students=[
 {
    "name":"Rafia Maqsood",
    "age":20
 },
 {
    "name":"Sawera",
    "age":36
 },
]

with open("student.json","w") as file:
    json.dump(students,file)


with open("student.json","r") as file:
    data = json.load(file)
print(data)