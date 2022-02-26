def endGame(res):
    '''Test if the word is the one searched

    :param res: string entered by the user when he/she test the word
    :type res: str

    :returns: If the word is full of 2
    :rtype: bool
    '''
    for i in res:
        if i != '2' : return False
    return True