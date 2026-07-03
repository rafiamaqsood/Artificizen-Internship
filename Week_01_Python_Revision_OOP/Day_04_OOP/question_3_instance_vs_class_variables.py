# Demonstrate the difference between instance and class variables: track how many objects of a class have been created. 

class Student:
    university= "University of Home Economics Lahore"
    object_count = 0  
    def __init__(self, name, age):
        self.name= name
        self.age= age
        Student.object_count += 1

student =Student("Rafia", 21)
print (student.name, student.age, student.university)
print("Total students created:", Student.object_count)

# university is a class varibale
# name and age are instance variable as each student have it's own name and age