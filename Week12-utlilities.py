def PrintOutput(words):
    print("OUTPUT",words)

def LoadFile(fileName):
    newList = []
    file = open(fileName,'r')
    lines = file.readlines()
    for i in lines:
        newList.append(i[0:-1])
    return newList
