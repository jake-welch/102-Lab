def PrintOutput(words):
    print("OUTPUT",words)

def LoadFile(fileName):
    newList = []
    file = open(fileName,'r')
    lines = file.readlines()
    for i in lines:
        newList.append(i[0:-1])
    return newList

def UpdateString(daString,letter,index):
    newString = ''
    a = 0
    for i in daString:
        if a != index:
            newString += i
        else:
            newString += letter
        a += 1
    print(newString)
