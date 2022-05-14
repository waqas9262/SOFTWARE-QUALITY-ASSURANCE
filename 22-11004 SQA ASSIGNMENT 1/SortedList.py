#22-11004



class SortedList:

    def __init__(self):

        self.sortedList = []




    def getLast(self):

        if len(self.sortedList) > 0:

            return self.sortedList[len(self.sortedList) - 1]   



    def getLength(self):

        return len(self.sortedList)  

    

    def getFirst(self):

        if len(self.sortedList) > 0:

            return self.sortedList[0]




    def removeHighest(self):

        if len(self.sortedList) == 0:

            return -1

        else:

            highest = self.sortedList[len(self.sortedList)-1]

            self.sortedList.remove(highest)

            return highest  





    def removeLowest(self):

        if len(self.sortedList ) == 0:

            return -1

        else:

            smallest = self.sortedList[0]

            self.sortedList.remove(smallest) 

            return smallest




    def insertNode(self, data):

        self.sortedList.append(data)

        self.sortedList.sort()

        return self.sortedList.index(data)


    def isEmpty(self):

        return len(self.sortedList) == 0
