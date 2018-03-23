# Chapter 26.03 for normal file
# Exception Handling
# Tianhe Zhang

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
	try:
		file = open("LOGS.car", "rb")
	except:
		raise NameError("File Not Found")

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

#############
# TASK 26.02
'''
import pickle

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

def createFile():
	newCar1 = CarRecord()
	newCar1.vhicleID = "499500"
	newCar1.registration = "abc"
	newCar1.dateRegist = "1999/12/28"
	newCar1.engineSize = 100
	newCar1.purchasePrice = 1000.02

	newCar2 = CarRecord()
	newCar2.vhicleID = "100112"
	newCar2.registration = "flk"
	newCar2.dateRegist = "1989/06/04"
	newCar2.engineSize = 200
	newCar2.purchasePrice = 13200.02

	newCar3 = CarRecord()
	newCar3.vhicleID = "549123"
	newCar2.registration = "grs"
	newCar2.dateRegist = "2001/09/11"
	newCar2.engineSize = 400
	newCar2.purchasePrice = 4569.78

	l1 = [newCar1, newCar2, newCar3]
	car_file = open('RAND.car', "wb")###
	car_file.close()
	car_file = open('RAND.car', "ab+")

	for i in range(len(l1)):
		cur_car = l1[i]
		addr = abs(hash(cur_car.vhicleID))
		car_file.seek(addr)
		print(len(pickle.dumps(cur_car)))
		pickle.dump(cur_car, car_file)

	car_file.close()

def find(vhicleID):
	r = []
	try:
		file = open("RAND.car", "rb")
	except:
		raise KeyError("File Not Found")
	for i in range(3):
		addr = abs(hash(vhicleID))
		print(addr)
		file.seek(addr)
		cur_car = pickle.load(file)
		r.append(cur_car)

	file.close()
	for i in range(len(r)):
		print(r[i])

createFile()
find('499500')
'''