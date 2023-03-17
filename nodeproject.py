from Button import*
import random
import time
import math
 
class Node:
    def __init__(self, x, y, win, name):
        self.center = Point(x, y)
        self.C = Circle(self.center, 30)
        self.neighbors = []
        self.name = name
        self.T = Text(self.center, self.name)
        self.nodeColor="white"
 
    def draw(self, win):
        self.C.draw(win)
        self.T.draw(win)
 
    def calcDegree(self):
        return len(self.neighbors)
 
    def getName(self):
        return self.name
 
    def undraw(self):
        self.C.undraw()
        self.T.undraw()
 
    def addNeighbor(self, n):
        self.neighbors.append(n)
 
    def getCenter(self):
        return self.center
 
    def getNeighbors(self):
        return self.neighbors
 
    def setNodeColor(self, c):
        self.C.setFill(c)
        self.nodeColor=c
       
 
    def printNeighbors(self):
        l = []
        for n in self.neighbors:
            l.append(n.getName())
        return l
 
    def getNodeColor(self):
        return self.nodeColor
 
class Graph:
 
    def __init__(self, n, e, win):
        self.nodes = []
        self.E = []
        Xpositions = []
        Ypositions = []
        self.names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
        numN = 0
        while True:
            x = random.randint(140, 740)
            y = random.randint(50, 550)
            foundNode = True
            for posX in Xpositions:
                if x - 70 < posX < x + 70:
                    for posY in Ypositions:
                        if y - 70 < posY < y + 70:
                            foundNode = False
            if foundNode:
                Xpositions.append(x)
                Ypositions.append(y)
                name = self.names.pop(0)
                N = Node(x, y, win, name)
                self.nodes.append(N)
                numN += 1
 
            if numN == n:
                break
 
        edges = 0
        while edges < e:
            n1 = random.choice(self.nodes)
            n2 = random.choice(self.nodes)
            if n1 != n2:
                if n1 not in n2.getNeighbors():
                    p1 = n1.getCenter()
                    p2 = n2.getCenter()
                    L = Line(p1, p2)
                    self.E.append(L)
                    L.draw(win)
                    edges += 1
                    n1.addNeighbor(n2)
                    n2.addNeighbor(n1)
 
        for node in self.nodes:
            node.draw(win)
            node.setNodeColor("white")
            #print(str(node.calcDegree()) + " : " + node.getName())
           
    def addNode(self, win):
        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        name = self.names.pop(0)
        N = Node(x, y, win, name)
        neighbor = random.choice(self.nodes)
        N.addNeighbor(neighbor)
        neighbor.addNeighbor(N)
        self.nodes.append(N)
        L = Line(Point(x, y), neighbor.getCenter())
        L.draw(win)
        self.E.append(L)
        neighbor.undraw()
        neighbor.draw(win)
        N.draw(win)
        N.setNodeColor("white")
 
    def removeNode(self, win):
        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        mouse = [x,y]
       
        for node in self.nodes:
            nodeX = node.getCenter().getX()
            nodeY = node.getCenter().getY()
            center = [nodeX, nodeY]
            #takes 2 lists with points, finds distance between them
            distance = math.dist(mouse, center)
            if distance <= 30:
                node.undraw()
                self.nodes.remove(node)
                for n in node.getNeighbors():
                    n.neighbors.remove(node)
                    for edge in self.E:
                        P1X = edge.getP1().getX()
                        P1Y = edge.getP1().getY()
                        P2X = edge.getP2().getX()
                        P2Y = edge.getP2().getY()
                        centerX = node.getCenter().getX()
                        centerY = node.getCenter().getY()
                        if P1X == centerX and P1Y == centerY:
                            edge.undraw()
                            self.E.remove(edge)
                        elif P2X == centerX and P2Y == centerY:
                            edge.undraw()
                            self.E.remove(edge)
 
    def addEdge(self, win):
        m = win.getMouse()
        x = m.getX()
        y = m.getY()
        mouse=[x,y]
        #idea was to set node1 to nothing(None) and based on the parameters, change it. if nothing changed
        #it would stay the same. Tried using this and it worked so stuck with it
        node1 = None
        for node in self.nodes:
            nodeX = node.getCenter().getX()
            nodeY = node.getCenter().getY()
            center = [nodeX,nodeY]
            distance = math.dist(mouse,center)
            if distance <= 30:
                node1=node
        if node1 == None:
            return 
        m2 = win.getMouse()
        x2 = m2.getX()
        y2 = m2.getY()
        mouse2=[x2,y2]
        node2=None
        for node in self.nodes:
            nodeX = node.getCenter().getX()
            nodeY = node.getCenter().getY()
            center = [nodeX,nodeY]
            distance2 = math.dist(mouse2,center)
            if distance2 <= 30:
                node2=node
        if node2==None:
            return 
        if node1==node2:
            return 
 
        if node2!=None:
            if node1 in node2.getNeighbors():
                return 
       
        L = Line(node1.getCenter(), node2.getCenter())
        L.draw(win)
        node1.undraw()
        node1.draw(win)
        node2.undraw()
        node2.draw(win)
        self.E.append(L)
        node1.addNeighbor(node2)
        node2.addNeighbor(node1)
               
    def Colors(self, win):
        for node in self.nodes:
            colorList = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Black", "White", "Cyan", "Salmon", "Tomato", "Beige"]
            nodecolorList = []
            for n in node.getNeighbors():
                if n.getNodeColor() not in nodecolorList:
                    nodecolorList.append(n.getNodeColor())
 
            for c in nodecolorList:
                if c in colorList:
                    colorList.remove(c)
            color = str(colorList[0])
            node.setNodeColor(color)
            #node.getColor=colorList[0]
               
                
            
            
                
        
 
   
    def minDegree(self):
        minD = 100
        for node in self.nodes:
            if node.calcDegree() < minD:
                minD = node.calcDegree()
        return minD
 
    def maxDegree(self):
        maxD = 0
        for node in self.nodes:
            if node.calcDegree() > maxD:
                maxD = node.calcDegree()
        return maxD
   
    def delete(self):
        for e in self.E:
            e.undraw()
        for n in self.nodes:
            n.undraw()
 
    def hasCycle(self):
        for n in self.nodes:
            #call traverse graph (recursive function) on each node in the graph
            #if it is every true (cycle found) return true.
            if self.traverseGraph(n, n, []):
                return True
        # if it never returned true, there was never a cycle
        return False
                       
    def traverseGraph(self, current, previous, visited):
        #base case -- dead end
        if len(current.getNeighbors()) <= 1:
            return False
 
        #see possible neighbors to still visit
        check = []
        for node in current.getNeighbors():
            # return true if one of the neighbors has been previously visited
            if (node in visited) and (node != previous):
                return True
            #otherwise, add unvisited nodes to a list to traverse
            elif node != previous:
                check.append(node)
               
        #update visited nodes 
        visited.append(previous)
        for node in check:
            #recursive call on each new unvisited neighbor
            if self.traverseGraph(node, current, visited):
                return True
        return False
               
        
        
def main():
 
    win = GraphWin("Graph Example", 800, 600)
    #buttons
    Q = Button(win, Point(20, 530), Point(100, 590), "tomato", "QUIT!")
    Gen = Button(win, Point(20, 430), Point(100, 490), "cyan", "Generate!")
    AddNode = Button(win, Point(20, 330), Point(100, 390), "beige", "Add Node")
    Degrees = Button(win, Point(20, 230), Point(100, 290), "beige", "Calc Degrees")
    Cycle = Button(win, Point(20, 130), Point(100, 190), "beige", "Has Cycle?")
    RemoveNode = Button(win, Point(20, 60), Point(100, 100), "Orange", "Remove Node")
    addEdge = Button(win, Point(120, 60), Point(200, 100), "Blue", "Add Edge")
    col = Button(win, Point(120, 130), Point(200, 190), "salmon", "Color!")
 
       
    G = Graph(1, 0, win)
    while True:
        m = win.getMouse()
        if Q.isClicked(m):
            break
        if Degrees.isClicked(m):
            print("Minimum Degree: " + str(G.minDegree()))
            print("Maximum Degree: " + str(G.maxDegree()))
        if Cycle.isClicked(m):
            if G.hasCycle():
                print("The graph has a cycle")
            else:
                print("The graph does not have a cycle")
        if Gen.isClicked(m):
            print("\n===================================\n")
            G.delete()
            #GRaph made with number of nodes and number of edges
            G = Graph(5, 4, win)
        if AddNode.isClicked(m):
            G.addNode(win)
        if RemoveNode.isClicked(m):
            G.removeNode(win)
        if addEdge.isClicked(m):
            G.addEdge(win)
        if col.isClicked(m):
            G.Colors(win)
        
           
    win.close()
 
if __name__ == "__main__":
    main()
