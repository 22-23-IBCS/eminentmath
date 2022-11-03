class grocery:
    def __init__(self, products, name, manager):
        self.p = products
        self.n = name
        self.m = manager


    def getlist(self):
        return list(self.p.keys())


    def purchase(self,l):
        money = 0
        for i in l:
            money = money + (self.p.get(i))
        return money
    
    def speak(self):
        print("Hi! Welcome" + "I am " + self.manager +
                  "How is your day")


def main():
    my = {"sandwitch" : 10,
          "hot pocket" : 3,
          "tater tots" : 8,
          "soup" : 6,
          "frozen yogurt" : 10,
          "coca cola" : 4,
          "fanta" : 4,
          "chetos" : 3,
          "takies" : 2,
          "pringles" : 3}

    
    store = grocery(my, "bobs gas station", "yashas")

    total = 0
    tobuy = []
    while True:
        question = input("what would you like to buy\n")
        if question == "speak to the manager":
            print(my.speak)
        
        if question == "stop":
            break
        else:
            tobuy.append(question)
            #print(my.get(question))
            #print("your total is\n" + str(my.purchase))
    price = store.purchase(tobuy)
    print("your total is\n"+str(price))
    
if __name__=="__main__":
    main()


            
    
    

    
