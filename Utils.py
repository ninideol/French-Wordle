"""
--> Utils :
    Some utils functions for the code.
"""

def ConvertListToDict(list):
    l = 65
    letterDict = {chr(i+65) : list[i] for i in range(0,len(list))}
    return letterDict

def sortDict(dict,rev = True):
    res = {key : val for key,val in sorted(dict.items(), key=lambda ele: ele[1], reverse= rev)}
    return res