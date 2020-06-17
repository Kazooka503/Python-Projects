class Employee:
    def __init__(self, first_name, last_name, email,
                 password, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.id_number = id_number

    def checkout(self):
        print("Calculating your total, please wait...")

    def promo(self):
        print("Calculating your rewards, please wait...")

class Clerk(Employee):

    def employee_discount(self):
        print("Calculating your discount, please wait...")

    def clock_in(self):
        print("Timecard Punched, get to work!")

class Manager(Employee):

    def refund(self):
        print("Calculating your refund, sorry for our mistake...")

    def supply_order(self):
        print("Order sent to commissary successful")

terry = Clerk("Terry", "Evans", "tbear@gmail.com", "SilverSpark123", "1")
print(terry.first_name + " " + terry.last_name)
print("Email: " + terry.email)
print("Password: " + terry.password)
print("ID#: " + terry.id_number)
terry.checkout()
terry.promo()
terry.employee_discount()
terry.clock_in()

print(" ")

casey = Manager("Casey", "Smith", "bdl@yahoo.com", "vintageoak", "2")
print(casey.first_name + " " + casey.last_name)
print("Email: " + casey.email)
print("Password: " + casey.password)
print("ID#: " + casey.id_number)
casey.checkout()
casey.promo()
casey.refund()
casey.supply_order()
