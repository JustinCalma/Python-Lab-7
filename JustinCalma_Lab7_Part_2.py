#Global Variables
MIN = 0
MAX = 0
firstInput = 0
secondInput = 0

#Main function
def main():
    getInput()
    calcSum()
    calcProduct()
    displayMinNum()
    displayMaxNum()
    calcDifference()
    calcQuotient()

#Get input and validate
def getInput():
    
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
    global firstInput
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
    global secondInput
    secondInput = int(b)

#Calculate Sum
def calcSum():
    sum = firstInput + secondInput
    print ("The sum is:" , sum)
    
#Calculate Product    
def calcProduct():
    product = firstInput * secondInput
    print ("The product is:" , product)
    
#Display Min
def displayMinNum():
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
    print ("The smaller number is", min)

#Display Max
def displayMaxNum():
    x = [firstInput , secondInput]
    max = 0
    for i in x:
        if i > max:
            max = i
    global MAX
    MAX = max
    print ("The bigger number is", max)

#Calculate Difference
def calcDifference():
    difference = MAX - MIN
    print ("The difference is", difference)

#Calculate Quotient
def calcQuotient():
    quotient = 0 
    if MIN <= 0:
        print ("You cannot divide by zero")
    else:
        quotient = MAX / MIN
        print ("The quotient of the two numbers is", quotient)



    
    
    
