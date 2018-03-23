from Class import *
import sys

BOOK = []
CD = []
BORROWER = []


def exitProgram():
	sys.exit(0)

def addBor():
	print("Input borrower name, email address, and id...")
	name = input("Name: ")
	email = input("Email: ")
	id = input("ID: ")
	newBor = Borrower(name, email, id)
	BORROWER.append(newBor)

def addBook():
	print("Input book name, author, and id...")
	name = input("Name: ")
	auther = input("Author: ")
	id = input("ID: ")
	newBook = Book(name, author, id)
	BOOK.append(newBook)

def addCD():
	print("Input CD name, author, and id...")
	name = input("Name: ")
	auther = input("Author: ")
	id = input("ID: ")
	newCD = CD(name, author, id)
	print("New CD has been created, please set genre...")
	genre = input("Genre")
	newCD.setGenre(genre)
	CD.append(newCD)

def borBook():
	curBor = None
	borID = int(input("Enter your ID: "))
	for bor in BORROWER:
		if bor.getBorrowerID() == borID:
			curBor = bor
	print('Input the book id...')
	id = int(input('Book id: '))
	for book in BOOK:
		if book.getItemID() == id:
			book.Borrow(curBor)
			break
			
	raise EOFError("Book not found!")

def retBook():
	bookID = int(input("Enter the book id: "))
	curBor = None
	borID = int(input("Enter the bor id: "))
	for bor in BORROWER:
		if borID == bor.getBorrowerID():
			curBor = bor
	for book in BOOK:
		if bookID == book.getItemID():
			book.Return(bor)
			break

def borCD():
	curBor = None
	borID = int(input("Enter your ID: "))
	for bor in BORROWER:
		if bor.getBorrowerID() == borID:
			curBor = bor
	print('Input the CD id...')
	id = int(input('CD id: '))
	for cd in CD:
		if cd.getItemID() == id:
			cd.Borrow(curBor)
			break

def retCD():
	cdID = int(input("Enter the CD id: "))
	curBor = None
	borID = int(input("Enter the bor id: "))
	for bor in BORROWER:
		if borID == bor.getBorrowerID():
			curBor = bor
	for cd in CD:
		if cdID == cd.getItemID():
			cd.Return(bor)
			break

def requestBook():
	boo = int(input("Input book id: "))
	for book in BOOK:
		if boo == book.getItemID():
			print(book)

def showINFO():
	for e in BOOK:
		print(e)
	for e in CD:
		print(e)
	for e in BORROWER:
		print(e)

def menu():
	menu_info = '''0 - Exit\n1 - Add a new borrower\n2 - Add a new book\n3 - Add a new CD\n
					4 - Borrow book\n5 - Return book\n6 - Borrow CD\n7 - Return CD
					8 - Request book\n9 - Show INFO\n'''
	m = {\
	0: exitProgram,\
	1: addBor,\
	2: addBook,\
	3: addCD,\
	4: borBook,\
	5: retBook,\
	6: borCD,\
	7: retCD,\
	8: requestBook,\
	9: showINFO}

	return menu_info, m

def main():

	Menu, menuDict = menu()
	books = []
	CDs = []
	borrowers = []
	# while True:
	print(Menu)
	print()
	input_choice = int(input("Enter 1-9 for your choice:\n"))
	choice = menuDict[input_choice].__call__()

while True:
	main()













