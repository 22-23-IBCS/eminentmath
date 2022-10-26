import random

class house:

    def __init__(self):
        self.rating = random.randint(1, 10)


    def getrating(self):
        return self.rating


def randpath(m, num):
    p = []


    while (len(p) < num):
        p = []

        x = random.randint(0,4)
        y = random.randint(0,4)
        p.append([x,y])
        pVal = m[x][y]
        


        for i in range(num - 1):

            neighbors = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
            bad = []
            for n in neighbors:
                if (n[0] > 4) or (n[0] < 0):
                    bad.append(n)
                elif (n[1] > 4) or (n[1] < 0):
                    bad.append(n)
                if n in p:
                    bad.append(n)
            for b in bad:
                neighbors.remove(b)

            if len(neighbors) == 0:
                break

            

            randN = random.choice(neighbors)
            p.append(randN)
            x = randN[0]
            y = randN[1]
            pVal += m[x][y]



    return pVal, p


def main():
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = house()
            l.append(h.getrating())

    print(m)
    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i])

    num = int(input("how many houses?\n"))

    pVal, p = randpath(m, num)

    ''' Greedy Path Call '''
#    pVal, p = greedyPath(m, num)

    print(p)

    ''' Random Path Call'''

    total = 0
    for i in range(5):
        for j in range(5):
            total = total + m[i][j]
    average = total/25

    while (average/25):
        pVal, p = randpath(m, num)
    while (average > pVal/num):
        pVal, p = randpath(m, num)

    print(p)

    print(" the avg value in the path is: " + str(pVal/num))
    print(" the avg value in the neighbour is: " + str(average))

    
if __name__ == "__main__":
    main()




