#demoReadFile.py
#V.Panigrahi
#demonstrate how to read files
#parse it for particular programs

def main():

    file=open("65094309.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        print(line)

main()
