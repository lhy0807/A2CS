# TASK 2.3 & 2.4 & 2.5
class Toy(object):

	def __init__(self, ID):
		self.__Name = ''
		self.__ID = ID 
		self.__Price = 0.00
		self.__MinimumAge = 0

	def setName(self, name):
		self.__Name = name

	def setPrice(self, price):
		self.__Price = price

	def setAge(self, age):
		if (0 <= age <= 18): self.__MinimumAge = age
		else: raise ValueError('Age not in range.')

	def getName(self):
		return self.__Name

	def getID(self):
		return self.__ID 

	def getPrice(self):
		return self.__Price 

	def getAge(self):
		return self.__MinimumAge

class ComputerGame(Toy):
	
	def __init__(self, ID):
		super().__init__(ID)
		self.__Category = ''
		self.__Console = ''

	def setCategory(self, new):
		self.__Category = new

	def setConsole(self, new):
		self.__Console = new

	def getCategory(self):
		return self.__Category

	def getConsole(self):
		return self.__Console

class Vehicle(Toy):

	def __init__(self, ID):
		super().__init__(ID)
		self.__Type = ''
		self.__Height = 0
		self.__Length = 0
		self.__Weight = 0.0

	def setType(self, t):
		self.__Type = t

	def setHeight(self, h):
		self.__Height = h

	def setLength(self, l):
		self.__Length = l

	def setWeight(self, w):
		self.__Weight = w

	def getType(self):
		return self.__Type

	def getHeight(self):
		return self.__Height

	def getLength(self):
		return self.__Length

	def getWeight(self):
		return self.__Weight

# Task 2.6
toys = []
v1 = Vehicle('RSC13')
v1.setName('Red Sports Car')
v1.setPrice(15.00)
v1.setAge(6)
v1.setType('Car')
v1.setHeight(3.3)
v1.setLength(12.1)
v1.setWeight(0.08)
toys += [v1]
c1 = ComputerGame('#steam233')
c1.setName('Dota2')
c1.setPrice(0)
c1.setAge(16)
c1.setCategory('MOBA')
c1.setConsole('/dota2_console')
toys += [c1] 

# TASK 2.7
def prompt():
	ID = str(input("Input toy ID: "))
	index = -1
	for i in range(len(toys)):
		if toys[i].getID() == ID:
			index = i 
	if index == -1:
		print("ID not found")
	else:
		toy = toys[index]
		print('ID:{} Name:{} Price:{} Minimum Age:{}'.format(toy.getID(),\
			toy.getName(),toy.getPrice(),toy.getAge()), end=' ')

		if isinstance(toy,ComputerGame):
			print('Category:{} Console:{}'.format(toy.getCategory(),\
				toy.getConsole()))

		else:
			print('Type:{} Heigth:{} Length:{} Weight:{}'.format(toy.getType(),\
				toy.getHeight(),toy.getLength(),toy.getWeight()))

# TASK 2.8
def enterDiscount():
	rate = int(input("Enter discount rate as %: "))
	for i in range(len(toys)):
		oldPrice = toys[i].getPrice()
		newPrice = toys[i].setPrice(oldPrice*(1-rate/100))
'''
enterDiscount()
prompt()
'''

# TASK 2.9
'''
Bubble sort: compare the forward value in the inner loop
Insertion sort: compare the backwrd value in the inner loop
'''

# Task 2.10
# bubble sort solution
def bubble(games): # games is where all the computer games stored
	for i in range(len(games)):
		for j in range(i, len(games)):
			if games[i].getPrice() > games[j].getPrice():
				temp = games[i]
				games[i] = games[j]
				games[j] = temp

# insertion sort solutions
def insertion(games):
	for i in range(1,len(games)):
		j = i - 1
		while (games[i].getPrice() < games[j].getPrice()) and (i > 0):
			temp = games[i]
			games[i] = games[j]
			games[j] = temp
			i -= 1

