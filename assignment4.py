class rewardPoints():
    '''This is a reward points account class'''
    def __init__(self, account_name = "Current Member", balance = 500):
        #protected 
        self._account_name = account_name
        #private
        self.__balance = balance

    def balanceGetter(self):
        print(self.__balance)

    def balanceSetter_redeem(self, value):
        if value <= self.__balance:
            self.__balance = self.__balance - value
            print("New balance: ", self.__balance)
        else:
            print("You do not have enough points!")

#object using protected and private attributes 
x = rewardPoints()

print(x._account_name)

while True:
    print("1. Check Rewards Balance")
    print("2. Redeem Points")
    menu_option = int(input())
    if menu_option == 1:
        x.balanceGetter()
    elif menu_option == 2:
        value = int(input("How many points would you like to redeem today? "))
        x.balanceSetter_redeem(value)
    else:
        print("Wrong menu choice!")


input()


