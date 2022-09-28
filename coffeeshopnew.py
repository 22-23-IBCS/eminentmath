class Coffeeshop:

    def __init__(self):
        self.coffee = 3
        self.latte = 4
        self.cider = 5

    def orderPrice(self, order):
        if order == "coffee":
            return self.coffee
        if order == "latte":
            return self.latte
        if order == "cider":
            return self.cider
        else:
            print("sorry, that is not on the menu")
        
        

    def askName(self, name):
        return name
        

def main():

    Cof = Coffeeshop()
    N = Coffeeshop()
    name = input("What is your name?\n")
    order = input("What would you like?\n")

    print("your total is: " + str(Cof.orderPrice(order)) + "$")
    print("Thank you, " + N.askName(name))



if __name__ == "__main__":
    main()
