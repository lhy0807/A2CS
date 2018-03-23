
import datetime


class Borrower(object):

	def __init__(self, n, e, i):
		self.__borrowerName = n
		self.__emailAddress = e
		self.__borrowerID = i
		self.__itemsOnLoan = 0

	def getBorrowerName(self):
		return self.__borrowerName

	def getEmailAddress(self):
		return self.__emailAddress

	def getBorrowerID(self):
		return self.__borrowerID

	def getItemsOnLoan(self):
		return self.__itemsOnLoan

	def updateLoan(self, n):
		self.__itemsOnLoan += n

	def __repr__(self):
		return '{}'.format(self.__dict__)

	def __eq__(self, other):
		if (self.__borrowerID == other.__borrowerID):
			return True
		else:
			return False

class LibraryItem(object):

	def __init__(self, t, a ,i):
		self.__title = t
		self.__auth = a 
		self.__itemID = i
		self.__onLoan = False
		self.__borrowerID = 0
		self.__dueDate = datetime.date.today()

	def getTitle(self):
		return self.__title

	def getAuth(self):
		return self.__auth

	def getItemID(self):
		return self.__itemID

	def getOnLoan(self):
		return self.__onLoan

	def getDueDate(self):
		return self.__dueDate

	def Borrow(self, bor):
		if x.getItemsOnLoan() <= 3:
			self.__onLoan = True
			self.__borrowerID = bor.getBorrowerID()
			self.__dueDate = self.__dueDate + datetime.timedelta(weeks=1)
			x.updateLoan(1)
		else:
			print("Max loan cannot exceed 3!!!")

	def Return(self, bor):
		self.__onLoan = False
		bor.updateLoan(-1)

	def __repr__(self):
		return "{}".format(self.__dict__)

class Book(LibraryItem):

	def __init__(self, t, a, i):
		super().__init__(t, a, i)
		self.__isRequested = False
		self.__requestedBy = 0

	def getIsRequested(self):
		return self.__isRequested

	def getRequestedBy(self):
		return self.__requestedBy

	def RequestBook(self, bor):
		self.__isRequested = True
		self.__RequestedBy = bor.getBorrowerID()

class CD(LibraryItem):

	def __init__(self, t, a, i):
		super().__init__(t, a, i)
		self.__genre = ""

	def getGenre(self):
		return self.__genre

	def setGenre(self, new):
		self.__genre = new