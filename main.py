import Utils
import wordlehelper
import temoin
import testWords

if __name__=='__main__':

    print("Welcome to this helper for Sutom and French Wordle !")

    #Initialisation of variables
    size = int(input("Size of the word ? "))
    fLetter = input("First Letter ? ([enter] if there is not) ")
    if fLetter != "": firstLetter = fLetter[0]
    else: firstLetter = '\n'
    theTemoin = temoin.create(size,firstLetter)
    toHave = []
    isFound = False

    while not isFound:
        #More variables
        letterDict = wordlehelper.countLetterByWordsWithCriterias(size,theTemoin,toHave)
        word = wordlehelper.findWords(size,letterDict,theTemoin,toHave)
        sortedDict = Utils.sortDict(word,False)
        bestWords = []

        print("Good Letter, Bad Place : ",toHave)

        #Find the best words and show them
        for i in range(10):
            if len(sortedDict) != 0:
                theWord = sortedDict.popitem()
                print(i," : ",theWord)
                bestWords.append(theWord)
            else : break
            
        wordNumber =  int(input("Word choosen ? (Number) "))
        word = bestWords[wordNumber]
        print("--->",word[0])
        print("How good is this word ? ")
        res = input("2 for Good place, 1 for Good Letter, 0 either : ")
        isFound = testWords.endGame(res)

    print("\n##> WELL DONE")