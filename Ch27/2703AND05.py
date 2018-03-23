import datetime

class LibraryItem(object):

	def __init__(self, t, a ,i):
		self.__Tilte = t
		self.__Author__Artist = a 
		self.__ItemID = i
		self.__OnLoan = False
		self.__DueDate = datetime.date.today()
		self.__BorrowerID = None

	def GetTitel(self):
		return self.__Tilte

	def borrowing(self, borrower):
		self.__OnLoan = True
		self.__BorrowerID = borrower.getID
		self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

	def Returning(self, borrower):
		borrower.updateItemsOnLoan(1)
		self.__BorrowerID = None
		self.__OnLoan = False

	def PrintDetails(self):
		print(self.__Tilte, ";", self.__Author__Artist, ";", end='')
		print(self.__ItemID, ";", self.__OnLoan, ";", self.__DueDate)

class Book(LibraryItem):
	
	def __init__(self, t, a, i):
		LibraryItem.__init__(self, t, a, i)
		self.__isRequested = False
		self.__RequestedBy = 0

	def GetIsRequested(self):
		return self.__IsRequested

	def SetIsRequested(self):
		self.__IsRequested = True

class CD(LibraryItem):

	def __init__(self, t, a, i):
		LibraryItem.__init__(self, t, a , i)
		self.__Genre = ""

	def GetGenre(self):
		return self.__Genre

	def SetGenre(self, g):
		self.__Genre = g

class Borrower(object):

	def __init__(self, name, addr, ID):
		self.borrowerName = name
		self.emailAddr = addr
		self.ID = ID
		self.onLoan = 0

	def getName(self):
		return self.borrowerName

	def getEmailAddr(self):
		return self.emailAddr

	def getID(self):
		return self.ID

	def getOnLoan(self):
		return self.onLoan

	def updateItemsOnLoan(self，inc):
		self.onLoan += inc


def main():
	# main function for the code
	
	CD_1 = CD("And Justice For All", "Metallica",10)
	CD_2 = CD("Dark Side of the Moon", "Pink Floyd", 20)
	CD_3 = CD("Black Sabbath", "Black Sabbath", 30)
	CD_4 = CD("Camila", "Camila Cabello",  40)
	CD_5 = CD("Havana", "Camila Cabello", 50)
	CDs = [CD_1, CD_2, CD_3, CD_4, CD_5]

	book_1 = Book("12 Rules for Life", "Jordan Peterson", 11)
	book_2 = Book("White Fang", "Jack London", 21)
	book_3 = Book("Great Expectations", "Charles Dickens", 31)
	book_4 = Book("The Joy Luck Club", "Amy Tan", 41)
	books = [book_1, book_2, book_3, book_4]

	for cd in CDs:
		cd.PrintDetails()

	for book in books:
		book.PrintDetails()

main()





