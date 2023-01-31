from graphics import *
from Button import *

def main():


    win = GraphWin("Python Challenge Problems", 800, 600)

    N1Text = Text(Point(80, 100), "Enter a noun")
    N1Text.draw(win)
    
    Noun1 = Entry(Point(200, 100), 20)
    Noun1.draw(win)

    N2Text = Text(Point(80, 200), "Enter a noun")
    N2Text.draw(win)

    Noun2 = Entry(Point(200, 200), 20)
    Noun2.draw(win)

    VText = Text(Point(80, 300), "Enter a verb")
    VText.draw(win)
    
    Verb = Entry(Point(200, 300), 20)
    Verb.draw(win)

    AText = Text(Point(75, 400), "Enter an adjective")
    AText.draw(win)
    
    Adjective = Entry(Point(200, 400), 20)
    Adjective.draw(win)

    EText = Text(Point(75, 500), "Enter an exclamation")
    EText.draw(win)

    Exclamation = Entry(Point(200, 500), 20)
    Exclamation.draw(win)

    B = Button(win, Point(400, 500), Point(520, 580), "tomato", "Generate!")

    while True:

        m = win.getMouse()

        if B.isClicked(m):
            noun1 = Noun1.getText()
            noun2 = Noun2.getText()
            verb = Verb.getText()
            adj = Adjective.getText()
            excl = Exclamation.getText()
            print(noun1)
            print(noun2)
            print(verb)
            print(adj)
            print(excl)




            
    


if __name__ == "__main__":
    main()
