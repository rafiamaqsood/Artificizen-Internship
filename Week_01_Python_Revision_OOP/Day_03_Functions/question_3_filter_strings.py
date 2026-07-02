#Use filter() to extract all strings longer than 5 characters from a list. 

stringss= ["Mouse", "Keyboard", " Printer" , "Monitor","USB"]
char5=list(filter(lambda i: len(i)>5, stringss))
print (char5)