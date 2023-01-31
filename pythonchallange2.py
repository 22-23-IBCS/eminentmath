from graphics import *
import time


def fall():
    win = GraphWin("fall", 400,600)
    x=200
    y=2
    ball = Circle(Point(x,y), 10)
    ball.draw(win)
    win.setBackground("White")
    while y<=600:
        ball.undraw()
        y=y**1.4
        ball = Circle(Point(x,y), 10)
        ball.draw(win)
        time.sleep(0.1)



def main():
    fall()



if __name__=="__main__":
    main()
