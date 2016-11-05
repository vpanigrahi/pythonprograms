name = input("What is your name: ")
age = int(input("What is your age:  "))
year = str((2016 - age) + 100)
j= int(input("How many times you want to print the previous message: "))
i = 0
while (i<j):
    print(name + " you will be 100 years on " + year)
    i=i+1
