nullPtr = -1

class Node(object):

	def __init__(self, data, ptr):
		self.data = data
		self.ptr = ptr

class LinkedList(object):

	def __init__(self, space):
		self.space = space
		self.startPtr = nullPtr
		self.freePtr = 0
		self.record = []
		for i in range(space):
			newNode = Node(None, i+1)
			self.record += [newNode]
		# set the last ptr
		self.record[-1].ptr = nullPtr

	def insert(self, value):
		if self.isFull(): 
			print("No space")
			return None
		else:		
			if (self.startPtr == nullPtr): # nothing has been inserted yet...
				self.startPtr = self.freePtr # set to 0
				self.freePtr = self.record[self.freePtr].ptr
				self.record[self.startPtr].data = value
				self.record[self.startPtr].ptr = nullPtr
			else: # there is something at first
				if (self.record[self.startPtr].data < value): # new value in the middle
					nextPtr = self.startPtr
					#print("check", nextPtr)
					while (self.record[nextPtr].data != None) and (self.record[nextPtr].data < value):
						prePtr = nextPtr
						nextPtr = self.record[nextPtr].ptr # increment index
						#print("check", nextPtr)
					tempFree1 = self.freePtr
					self.freePtr = self.record[self.freePtr].ptr
					self.record[tempFree1].data = value
					self.record[tempFree1].ptr = self.record[prePtr].ptr
					self.record[prePtr].ptr = tempFree1
				elif (self.record[self.startPtr].data > value): # new value at the first
					tempFree = self.freePtr
					self.freePtr = self.record[self.freePtr].ptr
					self.record[tempFree].data = value 
					self.record[tempFree].ptr = self.startPtr
					self.startPtr = tempFree
			self.space -= 1
				
	def isFull(self):
		if self.space == 1: return True
		return False

	def showNodes(self):
		tempPtr = self.startPtr
		while (tempPtr != nullPtr):
			print(self.record[tempPtr].data)
			tempPtr = self.record[tempPtr].ptr
		# for i in range(len(self.record)):
		# 	print(self.record[i].data)

	def find(self, value):
		tempPtr = self.startPtr
		while (tempPtr != nullPtr):
			if self.record[tempPtr].data == value:
				return tempPtr
			else:
				tempPtr = self.record[tempPtr].ptr
		return None 
		
	def delete(self, value):
		flag = self.find(value)
		if (flag != None):
			if (flag == self.startPtr): # if the delete is the first one
				tempFree = self.freePtr
				tempStart = self.startPtr
				self.startPtr = self.record[self.startPtr].ptr
				self.record[flag].data = None
				self.record[flag].ptr = self.freePtr
				self.freePtr = flag
			else: # in the middle or last
			# first we should find the previoius one
				nextPtr = self.startPtr
				while (nextPtr != nullPtr) and (self.record[nextPtr].data != value):
					prePtr = nextPtr
					nextPtr = self.record[nextPtr].ptr
				if (self.record[flag].ptr == nullPtr): # the last one
					self.record[prePtr].ptr = nullPtr
					self.record[flag].data = None
					self.record[flag].ptr = self.freePtr
					self.freePtr = flag
				else: # that's in the middle
					self.record[prePtr].ptr = self.record[flag].ptr
					self.record[flag].data = None
					self.record[flag].ptr = self.freePtr
					self.freePtr = flag


'''
Test functions
l = LinkedList(5)
l.insert(5)
l.insert(10)
l.insert(4)
l.insert(12)
l.delete(5)
l.delete(4)
l.delete(12)
l.showNodes()
		
'''
