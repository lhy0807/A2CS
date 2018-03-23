import pickle
import random

class CarRecord(object):

	def __init__(self):
		self.vhicleID = ""
		self.registration = ""
		self.dateRegist = None
		self.engineSize = 0
		self.purchasePrice = 0.00

	def __repr__(self):
		return \
		"vhicleID: {};\
		registration: {};\
		dateRegist: {};\
		engineSize: {};\
		purchasePrice: {}".format(self.vhicleID, self.registration, \
			self.dateRegist, self.engineSize, self.purchasePrice)

def write():
	cars = []
	length = 5
	for i in range(length):
		newCar = CarRecord()
		newCar.vhicleID = str(hash(i))
		newCar.registration = str(random.randint(0,1000))
		newCar.dateRegist = "12/28/1999"
		newCar.engineSize = random.randrange(5) * 10
		newCar.purchasePrice = float(random.randint(10000, 99999))
		cars.append(newCar)

	file = open("LOGS.car", "wb")
	for i in range(length):
		pickle.dump(cars[i], file)

	file.close()

def read():
	file = open("LOGS.car", "rb")

	cars = []
	length = 5
	i = 0
	while i < length:
		cars.append(pickle.load(file))
		i += 1
	return cars

def out():
	write()
	c = read()
	for i in range(len(c)):
		print(c[i])

out()



