# Calculate Area of a circle

pi = 3.14

def calcArea(r):
    return pi * r * r

r=8.7
print("Area of circle with radius: ",r," is ", calcArea(r))

r=9.2
print("Area of circle with radius: ",r," is ", calcArea(r))

r=16.03
print("Area of circle with radius: ",r," is ", calcArea(r))

print("++++++++++++++++++++++++++++++++++")

# Write function to check if a value exists in a list

data = ["python", "r", "java", "pascal", "c", "javascript", "assembly","html", "c++"]

def checkVal(search_el):
    for e in data:
        if e == search_el:
            return "Element is present in data list"
    return "Element not found"

print (checkVal("python"))
print (checkVal("html"))
print (checkVal("c"))


print("++++++++++++++++++++++++++++++++++")
# Write a function to shift list item to right n times

data = ["python", "r", "java", "pascal", "c", "javascript", "assembly", "html", "c++"]


def shiftItems(listName, n):
    shifted = listName[-n:] + listName[:-n]
    return shifted


print(data)
print(shiftItems(data, 3))
print(shiftItems(data, 1))


print("++++++++++++++++++++++++++++++++++")
# Use while loop to get data

#pi = 3.14

#def calcArea(r):
#    return pi * r * r

while True:
    r = input("Enter radius of circle or quit:" )
    if r =="quit":
        break
    else:
        print("Area of circle with radius: ",str(r)," is ",str(calcArea(float(r))))

print("++++++++++++++++++++++++++++++++++")

def totalMarks(subj1,subj2,subj3,subj4):
    return subj1+subj2+subj3+subj4
def getPercentage(marks):
    return  marks/4

def showDetails(**kwargs):
    print("Hello ", kwargs["name"])
    print("Here is your result for class of AI.")
    print("Your score card is as follows.")
    print("ClassMarks:")
    print("\tmath:",kwargs['marks']['math'])
    print("\tphysics:",kwargs['marks']['physics'])
    print("\tbiology:", kwargs['marks']['biology'])
    print("\tcomputer:", kwargs['marks']['computer'])
    totalmarks = totalMarks(kwargs['marks']['math'],kwargs['marks']['physics'],kwargs['marks']['biology'],kwargs['marks']['computer'])
    print("Total marks are: ",totalmarks)
    print("Percentage is as follows:",str(getPercentage(totalmarks)),"%")
    print("Maximum marks are in ","Biology")
    print("Minimum marks are in ","Math")
    print("You are promoted to next class .")

showDetails(name = "Ali",class_ = "AI",marks = {"math" : 50, "physics" : 80, "biology" : 90, "computer" : 67},date = "1 Feb 2020", nextClass = True)


