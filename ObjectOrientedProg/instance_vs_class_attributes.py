class Employee: 
    company = "Google" 
    salary = 100

bulbul = Employee() 
bulbul.name = "bulbul coder"
bulbul.company = "Microsoft" #instance attribute with same name as class attribute take prefrences over class attributes during assignment and retrieval
print(bulbul.name, bulbul.company, bulbul.salary)
    