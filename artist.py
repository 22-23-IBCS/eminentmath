import turtle

class drawings:
    def __init__(self,t):
        self.t = t

    def triangle(self, size = 100):
        for i in range(3):
            self.t.forward(100)
            self.t.right(120)
            self.t.forward(size)

    def square(self, size = 100):
        for i in range(4):
            self.t.forward(100)
            self.t.right(90)
            self.t.forward(size)

    def circle(self, size = 1):
        for i in range(360):
            self.t.right(1)
            self.t.forward(size)

    def star(self, size = 10):
        for i in range(5):
            self.t.forward(100)
            self.t.right(144)
            self.t.forward(size)

    def polygon(self, size = 1):
        for i in range (6):
            self.t.forward(100)
            self.t.right(60)
            self.t.forward(size)

    def pentagon(self, size = 1):
        for i in range(5):
            self.t.forward(100)
            self.t.right(72)
            self.t.forward(size)    
            
    def decagone(self, size = 1):
        for i in range (10):
            self.t.forward(100)
            self.t.right(72)
            self.t.forward(size)    
            
        

    
def main():
    canvas = turtle.Screen()
    canvas.bgcolor("white")
    canvas.title("Turtle")
    t = turtle.Turtle()
    t.speed(0)
    art = drawings(t)
    art.circle()
    art.square()
    art.triangle()
    art.star()
    art.polygon()
    art.pentagon()
    art.decagone()

if __name__=="__main__":
    main()
