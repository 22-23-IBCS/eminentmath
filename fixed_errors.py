import math

def greet():
    name = input("What's your name?\n")
    response = "Hello, {}. It is nice to meet you"
    print(response.format(name))

def circleArea(r):
    if r <= 0:
        return "Invalid circle dimensions"
    else:
        return math.pi*r**2

def studyMore(D):
    for student in D:
        if D[student] < 73:
            print(student + " needs to study more.")
    
def meanMedian(D):
    listOfGrades = list(D.values())
    listOfGrades.sort()
    total = sum(listOfGrades)
    mean = total/len(listOfGrades)
    median = listOfGrades[len(listOfGrades)//2]

    print("Average grade was: " + str(mean))
    print("Median grade was: " + str(median))
    
def main():
    D = {"Jake" : 90,
         "Betty" : 20,
         "Aristotle" : 100,
         "Genghis" : 25,
         "Shirley" : 88,
         "Salt" : 6,
         "Charlie" : 91,
         "Seacrest" : 72,
         "Ryan": 73}
    
    greet()
    print(circleArea(5))
    studyMore(D)
    meanMedian(D)


if __name__ == "__main__":
    main()


