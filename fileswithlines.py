def main():
    linesToRead = 5
    linesRead = 0

    userFileName = input("Please input the file name: ")
    print()

    readFile = open(userFileName, "r" )
    line = readFile.readline()
    linesRead = linesRead + 1


    while line != "" and linesRead <= linesToRead:
        print (line.rstrip("\n"))
        line = readFile.readline()
        linesRead = linesRead + 1

    readFile.close()

main()


