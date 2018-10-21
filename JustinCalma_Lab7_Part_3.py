#Global Variables
MIN = 0
MAX = 0

#Main function
def main():
    num1 = getNum()
    num2 = getNum()
    calcSum(num1, num2)
    calcProduct(num1, num2)
    displayMinNum(num1, num2)
    displayMaxNum(num1, num2)
    calcDifference(num1, num2)
    calcQuotient(num1, num2)

#Get input and validate
def getNum():
    a = input("enter number: ")
    run = False
    while run == False:
        counter = 0
        for char in a:
            if char.isdigit() == False:
                print("ERROR: Enter a positive integer")
                a = input("enter number: ")
                break
            counter = counter + 1
        if counter == len(a):
            run = True
    firstInput = int(a)
    return firstInput

#Calculate Sum
def calcSum(firstInput, secondInput):
    sum = firstInput + secondInput
    displayResult("Sum", sum)
    
#Calculate Product    
def calcProduct(firstInput, secondInput):
    product = firstInput * secondInput
    displayResult("Product", product)
    
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
    displayResult("Min", MIN)

#Display Max
def displayMaxNum(firstInput, secondInput):
    x = [firstInput , secondInput]
    max = 0
    for i in x:
        if i > max:
            max = i
    global MAX
    MAX = max
    displayResult("Max", MAX)

#Calculate Difference
def calcDifference(firstInput, secondInput):
    difference = MAX - MIN
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



    
    
    
