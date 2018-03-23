nullPtr = -1


class Node(object):

	def __init__(self):
		self.data = None
		self.leftPtr = nullPtr
		self.rightPtr = nullPtr

class BinaryTree(object):

	def __init__(self, space):
		self.space = space
		self.freePtr = 0
		self.rootPtr = nullPtr
		self.record = []
		for i in range(self.space): # initialize the tree
			newNode = Node()
			newNode.leftPtr = i + 1
			self.record += [newNode]
		# set the last node's left tree
		self.record[-1].leftPtr = nullPtr

	def insert(self, value):
		if (self.freePtr != nullPtr):
			newNodePtr = self.freePtr
			self.freePtr = self.record[self.freePtr].leftPtr
			self.record[newNodePtr].data = value # first set a temp value to a temp ptr
			self.record[newNodePtr].leftPtr = nullPtr # preset the next ptr
			self.record[newNodePtr].rightPtr = nullPtr # preset the next ptr
			if (self.rootPtr == nullPtr): self.rootPtr = newNodePtr
			else: # determine the left or right position for the temp ptr
				thisPtr = self.rootPtr
				while (thisPtr != nullPtr): # traking in the tree
					prePtr = thisPtr
					if (self.record[thisPtr].data > value):
						isLeft = True
						thisPtr = self.record[thisPtr].leftPtr
					else:
						isLeft = False # go right
						thisPtr = self.record[thisPtr].rightPtr
				if (isLeft): self.record[prePtr].leftPtr = newNodePtr
				else: self.record[prePtr]


	def find(self, value):
		thisPtr = self.rootPtr
		while (thisPtr != nullPtr) \
			and (self.record[thisPtr].data != value):

			if (self.record[thisPtr].data > value): thisPtr = self.record[thisPtr].leftPtr
			else: thisPtr = self.record[thisPtr].rightPtr

		return thisPtr
