number = int(input("Enter a number: "))
num = int(input("Enter a num to check: "))
check = int(input("enter a another number to divide by num: "))
if (number%2==0):
    print("Entered digit is even")
else:
    print("Entered digit is odd")

if(number%4==0):
    print("Entered Digit is a multiple of 4")
else:
    print("Entered Digit is not a multiple of 4")
    
if (num%check==0):
    print("Both num and check are evenly divisible")
else:
    print("Both num and check are not evenly divisible")
