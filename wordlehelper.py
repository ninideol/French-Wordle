import Utils

WORDS_NUMBER = 411430

def countLetterByWordsWithCriterias(size, temoin = [],goodLetter = []):
    f = open("mots.txt",'r')
    counter = [0 for i in range(26)]
    words = {}

    for i in range(WORDS_NUMBER):
        x = f.readline()
        isPossible = True
        if len(x) == size+1:
            for y in range(len(x)-1):
                if not temoin[y].__contains__(x[y]):
                    isPossible = False
                else:
                    for j in goodLetter:
                        if not x.__contains__(j):
                            isPossible = False
            if isPossible:
                alreadyRead = []
                for k in x[:-1]:
                    if k not in alreadyRead:
                        counter[ord(k)-65] += 1
    
    f.close()
    letterDict = Utils.ConvertListToDict(counter)
    return letterDict
    
def setTemoin(size,firstLetter = -1):
    temoin = []
    for i in range(size):
        temp = []
        for j in range(26):
            temp.append(chr(j+65))
        temoin.append(temp)
    if firstLetter != -1:
        temoin[0] = firstLetter
    return temoin
        
def findWords(size, letterDict, temoin = [],goodLetter = []) :
    f = open("mots.txt",'r')
    words = {}

    for i in range(WORDS_NUMBER):
        x = f.readline()
        isPossible = True
        if len(x) == size+1:
            for y in range(len(x)-1):
                if not temoin[y].__contains__(x[y]):
                    isPossible = False
                else:
                    for j in goodLetter:
                        if not x.__contains__(j):
                            isPossible = False
            if isPossible:
                score = 0
                alreadyRead = []
                for k in x[:-1]:
                    if k not in alreadyRead:
                        score += letterDict[k]
                        alreadyRead.append(k)
                words[x[:-1]] = score
                
    f.close()
    return words

# findWords(5)

# ALL LETTERS  
# A :  403734
# B :  60540
# C :  145834
# D :  97308
# E :  612711
# F :  52852
# G :  68140
# H :  52684
# I :  395674
# J :  7112
# K :  4905
# L :  168736
# M :  105440
# N :  303836
# O :  253639
# P :  98363
# Q :  22476
# R :  353551
# S :  424482
# T :  286929
# U :  152666
# V :  37828
# W :  1463
# X :  11059
# Y :  17590
# Z :  43156

# ALL LETTERS BY WORDS
# A :  290365 , 70.57458133825925
# B :  57874 , 14.066548380040347
# C :  129077 , 31.372773011204824
# D :  91802 , 22.3129086357339
# E :  353362 , 85.88629900590622
# F :  45139 , 10.971246627615876
# G :  64246 , 15.615293002454852
# H :  49864 , 12.119680139999515
# I :  278655 , 67.72841066524074
# J :  7083 , 1.7215565223731861
# K :  4572 , 1.111246141506453
# L :  137323 , 33.37700216318693
# M :  94592 , 22.991031281141385
# N :  224129 , 54.47560945968938
# O :  204590 , 49.72656344943246
# P :  88163 , 21.428432540164792
# Q :  22254 , 5.408939552293221
# R :  263089 , 63.94502102423255
# S :  266374 , 64.74345575188975
# T :  222879 , 54.171791070169895
# U :  138688 , 33.708771844542206
# V :  37019 , 8.99764236929733
# W :  1455 , 0.3536446054006757
# X :  11018 , 2.677976812580512
# Y :  17041 , 4.141895340641178
# Z :  42408 , 10.307464210193714

