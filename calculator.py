from addition import add
from subtraction import sub 
from division import div
from multiple import mult

print ("Welcome to Calculator Function")
print ("Choose option from menu:")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Division")

choice = int(input("Enter choice (1/2/3/4): "))

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if(choice is 1):
    print (add(num1,num2))

if (choice is 2):
    print (sub(num1, num2))

if(choice is 3):
    print (mult(num1,num2))

if (choice is 4):
    print (div(num1,num2))
