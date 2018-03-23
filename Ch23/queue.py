nullPtr = -1

class Node(object):

	def __init__(self, data, ptr):
		self.data = data
		self.ptr = ptr

class Queue(object):

	def __init__(self, space):
		self.space = space
		self.startPtr = nullPtr
		self.endPtr = nullPtr
		self.freePtr = 0
		self.record = []
		for i in range(space):
			newNode = Node(None, i+1)
			self.record += [newNode]
		# set the last ptr
		self.record[-1].ptr = nullPtr

	def enqueue(self, value): # add at the end
		if (self.startPtr == nullPtr): # there is nothing in the stack
			self.startPtr = self.freePtr # set to 0
			self.endPtr = self.startPtr
			self.freePtr = self.record[self.freePtr].ptr
			self.record[self.startPtr].data = value
			self.record[self.startPtr].ptr = nullPtr
		else: # there is something, so insert as the end
			self.record[self.endPtr].ptr = self.freePtr
			self.endPtr = self.freePtr
			self.freePtr = self.record[self.freePtr].ptr
			self.record[self.endPtr].data = value 
			self.record[self.endPtr].ptr = nullPtr


	def dequeue(self):
		value = self.record[self.startPtr].data # the value that is going to be deleted
		preStartPtr = self.startPtr
		self.record[self.startPtr].data = None
		self.startPtr = self.record[self.startPtr].ptr
		self.record[preStartPtr].ptr = self.record[self.freePtr].ptr
		self.freePtr = preStartPtr
		return value 





	# find the index of the seconde last element
	def findPre(self, lastPtr):
		nextPtr = self.startPtr
		while (nextPtr != lastPtr):
			prePtr = nextPtr
			nextPtr = self.record[nextPtr].ptr
		return prePtr

	# find the index of the last element
	def findLast(self):
		nextPtr = self.startPtr
		while (nextPtr != nullPtr): # get the ptr of the last one (prePtr)
			prePtr = nextPtr
			nextPtr = self.record[nextPtr].ptr
		return prePtr

	def showNodes(self):
		tempPtr = self.startPtr
		while (tempPtr != nullPtr):
			print(self.record[tempPtr].data)
			tempPtr = self.record[tempPtr].ptr
			
'''
#Test function
l = Queue(10)
l.enqueue(4)
l.enqueue(5)
l.enqueue(12)
l.enqueue(13)
print("check", l.dequeue())
l.showNodes()
'''