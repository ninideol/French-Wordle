from logging.config import stopListening
import Utils
import wordlehelper

size = int(input("Taille du mot ? "))
fLetter = input("Premire lettre ? ([entrer] si il n'y en a pas) ")
if fLetter != "": firstLetter = fLetter[0]
else: firstLetter = -1
temoin = wordlehelper.setTemoin(size,firstLetter)
toAvoid = []

def isITGood(word):
    print("How good is this word ? ")
    res = input("2 for Good place, 1 for Good Letter, 0 either : ")
    setTemoin(word,res)

def setTemoin(word,res):
    for i in range(len(res)):
        if res[i] == '2':
            temoin[i] = word[i]
        elif res[i] == '0':
            toAvoid.append(word[i])

while '?' in temoin:
    letterDict = wordlehelper.countLetterByWordsWithCriterias(size,toAvoid,-1)
    w = wordlehelper.findWords(size,letterDict,toAvoid,temoin)
    sortedDict = Utils.sortDict(w,False)
    bestWords = []
    for i in range(10):
        theWord = sortedDict.popitem()
        print(i," : ",theWord)
        bestWords.append(theWord)
    print(toAvoid)
    print(temoin)
    wordNumber =  int(input("Word choosen ? (Number) "))
    word = bestWords[wordNumber]
    print("--->",word[0])
    isITGood(word)
