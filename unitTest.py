import unittest
import temoin
import testWords



class SimpleTest(unittest.TestCase):

    def test(self):
        self.assertTrue(True)

    def test_create_temoin(self):
        temoinFive = []
        temoinOne = []
        tempTemoin = []
        for j in range(26):
            tempTemoin.append(chr(j+65))
        temoinOne.append(tempTemoin)
        for i in range(5):
            tempTemoin = []
            for j in range(26):
                tempTemoin.append(chr(j+65))
            temoinFive.append(tempTemoin)

        self.assertEqual(temoin.create(5),temoinFive)
        self.assertEqual(temoin.create(1),temoinOne)

    def test_endGame(self):
        goodWord5 = "22222"
        goodWord8 = "22222222"
        badWord5 = "20102"
        badWord10 = "Coucou c'est moi"
        self.assertTrue(testWords.endGame(goodWord5))
        self.assertTrue(testWords.endGame(goodWord8))
        self.assertFalse(testWords.endGame(badWord5))
        self.assertFalse(testWords.endGame(badWord10))

    def test_printTemoin(self):
        temoin1 = [['R'],['R','T']]
        temoin2 = [[],['T'],['E'],['S'],['T']]
        temoinEmpty = []
        self.assertEqual(temoin.printTemoin(temoin1),"R_")
        self.assertEqual(temoin.printTemoin(temoin2),"_TEST")
        self.assertNotEqual(temoin.printTemoin(temoin2),"R_")
        self.assertNotEqual(temoin.printTemoin(temoinEmpty),"R_")        

if __name__=='__main__':
    unittest.main()