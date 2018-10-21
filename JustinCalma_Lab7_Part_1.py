#Get two positive integer numbers and validate
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
a = int(a)
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
b = int(b)

#Add the two numbers and display the sum
sum = a + b
 
print("The sum of the two numbers is", sum)

#Multiply the two numbers and display the product
product = a * b

print("The product of the two numbers is", product)

#Display the bigger number
x = [a , b]
max = 0
for i in x:
    if i > max:
        max = i
print ("The bigger number is", max)

#Display the smaller number
x = [a , b]
if a == b:
    min = a
else:
    min = 0
    for j in x:
        if j < max:
            min = j
print ("The smaller number is", min)

#Subtract the smaller number from the bigger number and display
difference = max - min
print ("The difference is", difference)

#Divide the bigger number by the smaller number and display the result
quotient = 0 
if min <= 0:
    print ("You cannot divide by zero")
else:
    quotient = max / min
    print ("The quotient of the two numbers is", quotient) 

    
