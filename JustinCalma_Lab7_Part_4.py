#Global Variables
MIN = 0
MAX = 0

#Main function
def main():
    menu()

#Get input and validate
def getNums():
    
    a = input("enter first number: ")
    run = False
    while run == False:
        counter = 0
        for char in a:
            if char.isdigit() == False:
                print("ERROR: Enter a positive integer")
                a = input("enter first number: ")
                break
            counter = counter + 1
        if counter == len(a):
            run = True
    firstInput = int(a)
    
    b = input("enter second number: ")
    run = False
    counter = 0
    while run == False:
        for char in b:
            if char.isdigit() == False:
                print("ERROR: Enter a positive integer")
                b = input("enter second number: ")
                break
            counter = counter + 1
        if counter == len(b):
            run = True
    secondInput = int(b)
    return firstInput, secondInput

#Calculate Sum
def calcSum(firstInput, secondInput):
    sum = firstInput + secondInput
    displayResult("Sum", sum)
    return sum
    
#Calculate Product    
def calcProduct(firstInput, secondInput):
    product = firstInput * secondInput
    displayResult("Product", product)
    return product
    
#Display Min
def displayMinNum(firstInput, secondInput):
    x = [firstInput , secondInput]
    if firstInput == secondInput:
        min = firstInput
    else:
        min = 9999999
        for j in x:
            if j < min:
                min = j
    global MIN
    MIN = min
    return min

#Display Max
def displayMaxNum(firstInput, secondInput):
    x = [firstInput , secondInput]
    max = 0
    for i in x:
        if i > max:
            max = i
    global MAX
    MAX = max
    return max

#Calculate Difference
def calcDifference(firstInput, secondInput):
    num1 = displayMaxNum(firstInput, secondInput)
    num2 = displayMinNum(firstInput, secondInput)
    difference = num1 - num2
    displayResult("Difference", difference)

#Calculate Quotient
def calcQuotient(firstInput, secondInput):
    quotient = 0 
    if MIN <= 0:
        print ("You cannot divide by zero")
    else:
        quotient = MAX / MIN
        displayResult("Quotient", quotient)

#Display Result
def displayResult(resultName, resultValue):
    print (resultName, "is =", resultValue)

#Menu
def menu():
    print ("\n1- add")
    print ("2- multiply")
    print ("3- min")
    print ("4- max")
    print ("5- subtract")
    print ("6- divide")
    print ("7- quit")
    
    a = input("\nSelect function from display menu. ")
    run = False
    counter = 0
    while run == False:
        if a.isdigit() == False and (a < 1 or a > 7):
            print("ERROR: Enter a number between 1 and 7")     
            a = input("enter number: ")
        else:
            run = True
    firstInput = int(a)

    if firstInput == 1:
        num1, num2 = getNums()
        calcSum(num1, num2)        
    elif firstInput == 2:
        num1, num2 = getNums()
        calcProduct(num1, num2)
    elif firstInput == 3:
        num1, num2 = getNums()
        displayResult("Min", displayMinNum(num1, num2))
    elif firstInput == 4:
        num1, num2 = getNums()
        displayResult("Max", displayMaxNum(num1, num2))
    elif firstInput == 5:
        num1, num2 = getNums()
        calcDifference(num1, num2)
    elif firstInput == 6:
        num1, num2 = getNums()
        calcQuotient(num1, num2)
    elif firstInput == 7:
        quit()

    main()
    
main()    
