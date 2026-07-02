# Sort a list of dictionaries (e.g., students with name and marks) by marks using sorted() and a key function. 

students =[
    {
    "name" : "Rafia Maqsood",
     "Marks": 90},
     {
    "name" : "Sawera",
     "Marks": 89},
     {
    "name" : "Muneeba",
     "Marks": 91},
]
sorted_students = sorted(students,key=lambda x:x["Marks"])
print(sorted_students)