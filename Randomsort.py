import random

def main():

    L = [32, 14, 4, 90, 50, 55, 22, 78, 12]

    print(L)

    #sort with Bubble sort

    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                #swap
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
            print(L)

    while True:
        #sort with Random sort
        maxPos = len(L) - 1
        randomPos = randint(0, maxPos)
        #create a list with a random arrangement of the elements in the previous


        isSorted = True
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                isSorted = False

        if isSorted:
            break
        

if __name__ == "__main__":
    main()
