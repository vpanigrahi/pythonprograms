number = int(input("Enter a number you want to find divisors for: "))
newlist = []
listrange = list(range(1,number+1))
for num in listrange:
    if(number%num==0):
        newlist.append(num)
   
print(newlist)
