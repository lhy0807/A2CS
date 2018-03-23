'''
Stack and Queue Demo
Tianhe Zhang S3C2
'''
nullPtr = -1

class Node(object):

	def __init__(self, data, ptr):
		self.data = data
		self.ptr = ptr

class Stack(object):

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

	def push(self, value): 
		if (self.startPtr == nullPtr): 
			self.startPtr = self.freePtr 
			self.freePtr = self.record[self.freePtr].ptr
			self.record[self.startPtr].data = value
			self.record[self.startPtr].ptr = nullPtr
		else: 
			preStartPtr = self.startPtr
			self.startPtr = self.freePtr
			self.freePtr = self.record[self.freePtr].ptr
			self.record[self.startPtr].data = value 
			self.record[self.startPtr].ptr = preStartPtr

	def pop(self):
		tempStart = self.startPtr
		value = self.record[tempStart].data
		self.record[tempStart].data = None
		tempFree = self.freePtr
		self.freePtr = tempStart
		self.startPtr = self.record[self.startPtr].ptr
		self.record[tempStart].ptr = tempFree
		return value



	def showNodes(self):
		tempPtr = self.startPtr
		while (tempPtr != nullPtr):
			print(self.record[tempPtr].data)
			tempPtr = self.record[tempPtr].ptr
