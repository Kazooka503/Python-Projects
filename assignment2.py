class Employee:
    name = 'No Name Provided'
    email = ' '
    password = '123abcd'
    id_number = 0

class Clerk(Employee):
    pay = 15.00
    security_access = 'Low'

class Manager(Employee):
    pay = 22.00
    security_access = 'High'
    
