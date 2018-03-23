# Q1
# Tianhe Zhang
 

### a, i
class CustomerRecord(object):

	def __init__(self, ID, name, tel, order):
		self.ID = ID
		self.name = name
		self.tel = tel
		self.order = order

### a, ii
CustomerData = [None for i in range(0,1000)]

### b, i
def Hash(ID):
	addr = ID % 1000
	return addr		

### b, ii
def AddRecord(Customer):
	addr = Hash(Customer.ID)
	while CustomerData[addr] != None:
		addr += 1
		if addr >= 1000:
			addr = 0
	CustomerData[addr] = Customer

### b, iii
def FindRecord(CustomerID):
	addr = Hash(CustomerID)
	while CustomerID != CustomerData[addr].ID:
		addr += 1
		if addr >= 1000:
			addr = 0
	Customer = CustomerData[addr]
	return Customer



