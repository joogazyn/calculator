def mult(n1,n2):
    r = (n1*n2)
    print "The answer is = "+str(r)


print "Welcome to Calculator Function"
print "Menu:"
print "1. Add"
print "2. Subtract"
print "3. Multiply"
print "4. Division"

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))


if(choice is 3):
    mult(num1,num2)
