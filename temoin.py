def create(size,firstLetter = '\n'):
    '''Create the temoin of the word and then return it

    :param size: size of the word
    :type size: int
    :param firstLetter: first letter of the word
    :type firstLetter: char

    :returns: the temoin of this new word considering the parameters
    :rtype: str list list
    '''
    temoin = []
    for i in range(size):
        temp = []
        for j in range(26):
            temp.append(chr(j+65))
        temoin.append(temp)
    if firstLetter != '\n':
        temoin[0] = [firstLetter]
    return temoin

def setTemoin(temoin,toHave,word,res):
    '''Set the temoin using word choosen and how good it is

    :param temoin:
    :type temoin: str list list
    :param toHave: good letters missplaced in the word
    :type toHave: char list
    :param word: word choosen by the user
    :type word: str
    :param res: goodeness of the word choosen
    :type res: str

    :returns: the temoin and the letter to Have and missplaced
    :rtype: str list list, char list tuple
    '''
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
    return (temoin,toHave)

def printTemoin(temoin):
    '''
    :param temoin:
    :type temoin: str list list
    
    :returns: the words good written with '_' as blank spaces
    :rtype: string
    '''
    toWrite = ""
    for i in temoin:
        if len(i) != 1: toWrite += "_"
        else: toWrite += i[0]
    return toWrite

def t:
	return 1
