import Utils
import wordlehelper
import temoin
import testWords

def printError(number,theTemoin=""):
    print("\n--ERROR--")
    if number==0:
        print("According to our database, there is no words left =(")
        print("Your word looks like this : ", temoin.printTemoin(theTemoin))
    if number==1:
        print("Your choice is too high or too low =(")
        print("Try another one !")
    print("--ERROR--\n")

if __name__=='__main__':

    print("Welcome to this helper for Sutom and French Wordle !")

    #Initialisation of variables
    size = int(input("Size of the word ? "))
    fLetter = input("First Letter ? ([enter] if there isn't) ")
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

        #Find the best words and show them
        for i in range(10):
            if len(sortedDict) != 0:
                theWord = sortedDict.popitem()
                print(i," : ",theWord)
                bestWords.append(theWord)
            else : break
            
        #Check if there is words
        if len(bestWords) == 0 : 
            printError(0,theTemoin)
            break

        wordNumber =  int(input("Word choosen ? (Number) "))

        #Check if the input is possible
        if wordNumber > len(bestWords)-1 or wordNumber < 0:
            printError(1)
            continue

        word = bestWords[wordNumber]
        print("--->",word[0])
        print("How good is this word ? ")
        res = input("2 for Good place, 1 for Good Letter, 0 either : ")
        isFound = testWords.endGame(res)
        (theTemoin,toHave) = temoin.setTemoin(theTemoin,toHave,word[0],res)

    if isFound: print("\n##> WELL DONE")