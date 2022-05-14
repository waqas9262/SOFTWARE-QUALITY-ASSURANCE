#22-11004

import unittest
from SortedList import SortedList 

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        self.testList = SortedList()
        self.testList.insertNode(2)
        self.testList.insertNode(1)
        self.testList.insertNode(5)
        self.testList.insertNode(3)
        

    def test1(self):

        if (self.testList.isEmpty() == False):
            print("isEmpty() providing correct information about list")
        else:
            print("isEmpty() not providing correct information about list")



    def test2(self):

        supposedRemoved = self.testList.getLast()

        if (self.testList.removeHighest() == supposedRemoved):
            print("removeHighest() removing hiughest value correctly")
        else:
            print("removeHighest() not removing hiughest value correctly")





    def test3(self):

        if (self.testList.getLength() == 4):
            print("getLength() giving correct length of list")
        else:
            print("getLength() not providing correct length of list because of some instances")


    



    def test4(self):

        if (self.testList.insertNode(4) == 3):
            print("insertNode() adding new element correctly")
        else:
            print("insertNode() not adding new element correctly")



    def test5(self):

        supposedRemoved = self.testList.getFirst()

        if (self.testList.removeLowest() == supposedRemoved):
            print("removeLowest() removing lowest value correctly")
        else:
            print("removeLowest() not removing lowest value correctly")

if __name__ == "__main__":

    tester = SimpleTestCase()
    tester.setUp()
    tester.test3()
    tester.test4()
    tester.test5()
    tester.test2()
    tester.test1()
    unittest.main()
