a = [ 1, 2, 3, 55, 88, 65, 41, 12, 8, 5]
number = int(input("Enter a number you want the elements lesser than: "))
newlist = []

for i in a:
    if i<number:
        newlist.append(i)

print (newlist)
