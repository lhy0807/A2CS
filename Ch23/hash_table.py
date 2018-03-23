class HashTable(object):

	def __init__(self, size):
		self.size = size
		self.table = [None for i in range(self.size)]
		self.maxIndex = self.size - 1

	def hashing(self, val):
		address = val % self.size
		return address

	def insert(self, newRecord):
		index = self.hashing(newRecord)
		while self.table[index] != None:
			index += 1
			if index > self.maxIndex:
				index = 0
		self.table[index] = newRecord

	def findRecord(self, searchKey):
		index = self.hashing(searchKey)
		while (self.table[index] != searchKey) \
			and (self.table[index] != None):

			index += 1
			if index > self.maxIndex:
				index = 0

		if self.table[index] != None:
			return self.table[index]

l = HashTable(10)
l.insert(2345)
print(l.findRecord(2345))
l.insert(98765432)
print(l.findRecord(33))
l.insert(5)
print(l.findRecord(5))


