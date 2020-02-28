class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def Inbetween(self,middle_node,newdata):
		if middle_node is None:
			print("The mentioned node is absent")
			return
		newnode = Node(newdata)
		newnode.nextval = middle_node.nextval
		middle_node.nextval = newnode

    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
    	if self.headval is None:
        	self.headval = NewNode
        	return
		lastval = self.headval
		while(curval.nextval):
			lastval = curval.nextval
		lastval.nextval = Node(newdata)

    def Remove(self, Removekey):

		HeadVal = self.headval
		if HeadVal is not None:
			if HeadVal.dataval == Removekey:
				self.headval = HeadVal.nextval
				HeadVal = None
				return
		while (HeadVal is not None):
			if HeadVal.dataval == Removekey:
				break
			prev = HeadVal
			HeadVal = HeadVal.nextval

		if (HeadVal == None):
			return
		prev.nextval = HeadVal.nextval
		HeadVal = None
    		




if __name__ == "__main__":
	list1 = SLinkedList()
	list1.headval = Node("Mon")
	e2 = Node("Tue")
	e3 = Node("Wed")

	# Link first Node to second node
	list1.headval.nextval = e2

	# Link second Node to third node
	e2.nextval = e3

	list1.AtBegining("Sun")
	list1.AtEnd("Thursday")
	list1.Inbetween(e2, "Friday")
	list1.Remove('Friday')
	list1.Remove('Sun')
	list1.Remove('Tue')
	list1.listprint()
