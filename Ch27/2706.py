import datetime

class LibraryItem(object):

	def __init__(self, t, a ,i):
		self.__Tilte = t
		self.__Author__Artist = a 
		self.__ItemID = i
		self.__OnLoan = False
		self.__DueDate = datetime.date.today()

	def GetTitel(self):
		return self.__Tilte

	def borrowing(self):
		self.__OnLoan = True
		self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

	def Returning(self):
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

	def SetIsRequested(self, borrower):
		self.__RequestedBy = borrower
		self.__IsRequested = True
	
	def PrintDetails(self):
		print(self.__Tilte, ";", self.__Author__Artist, ";", end='')
		print(self.__ItemID, ";", self.__OnLoan, ";", self.__DueDate)
		print(self.__isRequested, self.__RequestedBy)

class CD(LibraryItem):

	def __init__(self, t, a, i):
		LibraryItem.__init__(self, t, a , i)
		self.__Genre = ""

	def GetGenre(self):
		return self.__Genre

	def SetGenre(self, g):
		self.__Genre = g
	
	def PrintDetails(self):
		print(self.__Tilte, ";", self.__Author__Artist, ";", end='')
		print(self.__ItemID, ";", self.__OnLoan, ";", self.__DueDate) 
		print(self.__Genre)

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





