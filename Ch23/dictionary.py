class DicEle(object): # a single element in a dictionary

	def __init__(self, key, value):
		self.key = key
		self.value = value

class Dictionary(object):

	def __init__(self, size):
		self.size = size
		self.maxIndex = self.size - 1
		self.dicList = [None for i in range(self.size)]

	def hashing(self, value):
		if isinstance(value, str):
			# do the str has
			return ord(value[-1]) % 10
		elif isinstance(value, int):
			pass

	def insert(self, newKey, newValue):
		newEntry = DicEle(newKey, newValue)
		index = self.hashing(newKey) # generate index
		while (self.dicList[index] != None):
			index += 1
			if (index > self.maxIndex):
				index = 0
		self.dicList[index] = newEntry

	def find(self, searchKey):
		index = self.hashing(searchKey)
		while (self.dicList[index] != None) and \
			(self.dicList[index].key != searchKey):

			index += 1 # not in general location
			if (index > self.maxIndex):
				index = 0

		if (self.dicList[index] != None):
			return self.dicList[index].value

	def show(self):
		for i in range(self.size):
			if (self.dicList[i] != None):
				print(self.dicList[i].key, "-->",self.dicList[i].value)
		print("--Dic showed.--\n")

def test():
	newDic = Dictionary(10)
	newDic.insert("alu", "arithematic logic unit")
	newDic.insert("IP", "Internet Protocol")
	newDic.insert("exp", "exponent")
	newDic.insert(".","AND")
	newDic.insert("+", "OR")
	newDic.show()
	print(newDic.find("+"))
	print(newDic.find("/"))
	print(newDic.find("alu"))

test()

