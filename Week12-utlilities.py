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
    
def FindWordCount(someList, word):
    counter = 0
    newList = []
    for i in someList:
        newList.append(i.split())
    for i in newList:
        for a in i:
            if a.lower() == word.lower():
                counter += 1
    PrintOutput(counter)

def ScoreFinder(players, scores, name):
    a = 0
    true = 0
    score = 0.0
    output = ''
    for i in players:
        if i.lower() == name.lower():
            true = 1
            break
        a += 1
    if true == 1:
        score = scores[a]
        output = (players[a] + ' got a score of ' + str(score))
        PrintOutput(output)
    else:
        PrintOutput('player not found')
