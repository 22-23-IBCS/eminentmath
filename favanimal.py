class favourateanimal:

    def __init__(self,kind,owner,specie,color,age):
        self.kind=kind
        self.owner=owner
        self.specie=specie
        self.color=color
        self.age=age




    def setowner(self,owner):
        self.owner=owner



    def getowner(self):
        return self.owner


    def setcolor(self,color):
        self.color=color


    def getcolor(self):
        return self.color


def main():
    animal1=favourateanimal("snake","yashas","reptile","black","10")
    animal1.setowner("tom")
    print(animal1.getowner())
    animal1.setcolor("green")
    print(animal1.getcolor())

    animal2=favourateanimal("bear","yashas","mammal","black","12")
    animal2.setowner("ron")
    print(animal2.getowner())
    animal2.setcolor("brown")
    print(animal2.getcolor())

print(main())
        
        

        
        

