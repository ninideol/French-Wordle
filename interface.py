from logging.config import stopListening
import Utils
import wordlehelper

size = int(input("Taille du mot ? "))
fLetter = input("Premire lettre ? ([entrer] si il n'y en a pas) ")
if fLetter != "": firstLetter = fLetter[0]
else: firstLetter = -1
temoin = wordlehelper.setTemoin(size,firstLetter)
toHave = []
isFound = False

def isITGood(word):
    print("How good is this word ? ")
    res = input("2 for Good place, 1 for Good Letter, 0 either : ")
    setTemoin(word,res)

def setTemoin(word,res):
    alreadyTried = []
    for i in range(len(res)):
        if res[i] == '2':
            temoin[i] = [word[i]]
            alreadyTried.append(word[i])
        elif res[i] == '1':
            toHave.append(word[i])
            temoin[i].remove(word[i])
            alreadyTried.append(word[i])
        elif res[i] == '0':
            if word[i] not in alreadyTried:
                for k in temoin:
                    if word[i] in k: k.remove(word[i])
            alreadyTried.append(word[i])

while not isFound:
    letterDict = wordlehelper.countLetterByWordsWithCriterias(size,temoin,toHave)
    w = wordlehelper.findWords(size,letterDict,temoin,toHave)
    sortedDict = Utils.sortDict(w,False)
    bestWords = []
    print(toHave)
    for i in range(10):
        if len(sortedDict) != 0:
            theWord = sortedDict.popitem()
            print(i," : ",theWord)
            bestWords.append(theWord)
        else : break
    wordNumber =  int(input("Word choosen ? (Number) "))
    word = bestWords[wordNumber]
    print("--->",word[0])
    isITGood(word[0])

print("\n##> BRAVO VOUS AVEZ TROUVÉ")
