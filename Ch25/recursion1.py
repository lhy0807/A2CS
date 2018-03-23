
def factorial(n):
	if (n == 0):
		return 1
	else:
		return n * factorial(n-1)

def bunnyEars(bunnies):
	if (bunnies == 0): return 0
	return bunnyEars(bunnies - 1) + 2

def fibonacci(n):
	if (n == 0): return 0
	elif (n == 1): return 1
	return fibonacci(n-2) + fibonacci(n-1)

def bunnyEars2(bunnies):
	if (bunnies == 0): return 0 # base
	if (bunnies % 2 == 0): return bunnyEars2(bunnies - 1) + 3
	if (bunnies % 2 == 1): return bunnyEars2(bunnies - 1) + 2

def triangle(rows):
	if (rows == 0): return 0
	else:
		return rows + triangle(rows - 1)

def sumDigit(n):
	if (n//10==0): return n
	else:
		return n%10 + sumDigit(n//10)

def count7(n):
	if (n==7): return 1
	if (n//10==0 and n!=7): return 0
	else:
		return count7(n%10) + count7(n//10)

def count8(n):
	if (n%10 == n and n != 8): return 0
	else:
		if (n%10 == 8 and (n//10)%10 == 8):
			return 3 + count8(n//100)
		elif (n%10 == 8 and (n//10)%10 != 8):
			return 1 + count8(n//10)
		else:
			return count8(n%10) + count8(n//10)

def powerN(base, n):
	if (n==0): return 1
	else:
		return base * powerN(base, n-1)



def countX(s):
	if (len(s) == 1):
		if s=="x": return 1
		else: return 0
	else:
		return countX(s[-1]) + countX(s[:-1])

def countHi(s):
	if len(s)==0: return 0
	else:
		if (s[0]=="h" and s[1]=="i"):
			return 1 + countHi(s[2:])
		else:
			return 0 + countHi(s[1:])

def changeXY(s):
	if (len(s) == 0): return ''
	if (len(s) == 1):
		if (s=="x"): return "y"
		if (s=="y"): return "x"
		else: return s
	else:
		return changeXY(s[0]) + changeXY(s[1:])

def changePi(s):
	if (len(s) <= 1): return s
	else:
		if (s[0] == "p" and s[1] == "i"):
			return "3.14" + changePi(s[2:])
		else:
			return s[0] + changePi(s[1:])

def noX(s):
	if (s=="x"): return ""
	if (len(s) == 1): return s
	else:
		return noX(s[0]) + noX(s[1:])

def array6(nums, i):
	nums = nums[i:]
	if (len(nums) == 0): return False
	if (len(nums) == 1): 
		if nums == [6]: return True
		else: return False
	else:
		return array6(nums[:1],0) or array6(nums,1)

def array11(nums, i):
	nums = nums[i:]
	if (len(nums) == 0): return 0
	if (len(nums) == 1):
		if (nums == [11]): return 1
		else: return 0
	else:
		return array11(nums[:1],0) + array11(nums[1:],0)

def array220(nums, i):
	if (len(nums) <= 1): return False
	else:
		if (nums[0]*10 == nums[1]):
			return True
		else:
			return array220(nums[1:],0) or array220(nums[1:],0)

def allStar(s):
	if (len(s) <= 1): return s
	else:
		return s[0]+"*"+allStar(s[1:])

def pairStar(s):
	if (len(s) <= 1): return s
	else:
		if (s[0] == s[1]):
			return s[0] + "*" + pairStar(s[1:])
		else:
			return s[0] + pairStar(s[1:])

def endX(s):
	if (len(s) == 0): return s
	else:
		if (s[0] == "x"):
			return endX(s[1:]) + "x"
		else:
			return s[0] + endX(s[1:])

def countPairs(s):
	if (len(s) <= 2): return 0
	else:
		if (s[0] == s[2]):
			return 1 + countPairs(s[1:])
		else:
			return countPairs(s[:1]) + countPairs(s[1:])

def countAbc(s):
	if (len(s) <= 2): return 0
	else:
		if (s[0:3] == "abc" or s[0:3] == "aba"):
			return 1 + countAbc(s[2:])
		else:
			return countAbc(s[:1]) + countAbc(s[1:])

def count11(s):
	if (len(s) <= 1): return 0
	else:
		if (s[0] == "1" and s[1] == "1"):
			return 1 + count11(s[2:])
		else:
			return count11(s[0]) + count11(s[1:])

def stringClean(s):
	if (len(s) <= 1): return s
	else:
		if (s[0] == s[1]):
			return stringClean(s[1:])
		else:
			return s[0] + stringClean(s[1:])

def countHi2(s):
	if (len(s) <= 1): return 0
	else:
		if (s[0] == "x" and s[1:3] == "hi"):
			return 0 + countHi2(s[3:])
		elif (s[:2] == "hi"):
			return 1 + countHi2(s[2:])
		else:
			return 0 + countHi2(s[1:])

def parenBit(s):
	if (len(s) <= 1): return ""
	if (s[0] == "(" and s[-1] == ")"): return s[:]
	else: 
		if s[0] == "(" and s[-1] != ")":
			return parenBit(s[:-1])
		if s[0] != "(" and s[-1] == ")":
			return parenBit(s[1:])
		else:
			return parenBit(s[1:-1])
			
def nestParen(s):
	return 42

def strCount(s1, s2):
	return 42

def strCopies(s1, s2, n):
	return 42

def strDist(s1, s2):
	return 42

### END ###

### Test functions ###

def testCountHi():
	assert(countHi("xxhixixi") == 1)
	assert(countHi("xhixhi") == 2)

def testChangeXY():
	print("testing changeXY...", end="")
	assert(changeXY("") == "")
	assert(changeXY(" ") == " ")
	assert(changeXY(" x ") == " y ")
	assert(changeXY("codex") == "codey")
	assert(changeXY("xxhixx") == "yyhiyy")
	assert(changeXY("xhixhix") == "yhiyhiy")
	print("Passed.")

def testChangePi():
	print("testing changePi...", end="")
	assert(changePi("xpix") == "x3.14x")
	assert(changePi("pipi") == "3.143.14")
	assert(changePi("pip") == "3.14p")
	assert(changePi("ppphi") == "ppphi")
	print("Passed.")

def testNoX():
	print("testing noX...", end="")
	assert(noX("xaxb") == "ab")
	assert(noX("ab c") == "ab c")
	assert(noX("xxxxVxxxx") == "V")
	print("Passed.")

def testArray6():
	print("testing array6...", end="")
	assert(not array6([],0))
	assert(array6([1,6,4],0))
	assert(not array6([1,4],0))
	assert(array6([6],0))
	assert(not array6([6,6,6,1,5,7],3))
	print("Passed.")

def testArray11():
	print("testing array11...", end="")
	assert(array11([1,2,11],0) == 1)
	assert(array11([11,11],0 == 2))
	assert(array11([1,2,3,4],0) == 0)
	print("Passed.")

def testArray220():
	print("testing array220...", end="")
	assert(array220([1,2,20],0))
	assert(array220([3,30], 0))
	assert(not array220([3],0))
	print("Passed.")

def testAllStar():
	print("testing allStar...",end='')
	assert(allStar("") == "")
	assert(allStar(" ") == " ")
	assert(allStar("ab") == "a*b")
	assert(allStar("abc") == "a*b*c")
	assert(allStar("hello") == "h*e*l*l*o")
	print("Passed.")

def testPairStar():
	print("testing pairStar...",end='')
	assert(pairStar("hello") == "hel*lo")
	assert(pairStar("xxyy") == "x*xy*y")
	assert(pairStar("aaaa") == "a*a*a*a")
	print("Passed.")

def testEndX():
	print("testing endX...", end="")
	assert(endX("rexx") == "rexx")
	assert(endX("xxre") == endX("rexx"))
	assert(endX("xxhixx") == "hixxxx")
	assert(endX("xhixhix") == "hihixxx")
	print("Passed.")

def testCountPairs():
	print("testing countPairs...", end="")
	assert(countPairs("axa") == 1)
	assert(countPairs("axax") == 2)
	assert(countPairs("axbx") == 1)
	assert(countPairs("hi") == 0)
	assert(countPairs("hihih") == 3)
	assert(countPairs("ihihhh") == 3)
	assert(countPairs("ihjxhh") == 0)
	assert(countPairs("") == 0)
	assert(countPairs("a") == 0)
	assert(countPairs("aa") == 0)
	assert(countPairs("aaa") == 1)
	print("Passed.")

def testCountAbc():
	print("testing countAbc...", end="")
	assert(countAbc("abc") == 1)
	assert(countAbc("abcxxabc") == 2)
	assert(countAbc("abaxxaba") == 2)
	assert(countAbc("abcabc") == 2)
	assert(countAbc("ababc") == 2)
	assert(countAbc("abxbc") == 0)
	assert(countAbc("aaabc") == 1)
	assert(countAbc("hello") == 0)
	assert(countAbc("") == 0)
	assert(countAbc("ab") == 0)
	assert(countAbc("aba") == 1)
	assert(countAbc("aca") == 0)
	assert(countAbc("aaa") == 0)
	print("Passed.")

def testCount11():
	print("testing count11...", end="")
	assert(count11("abc11x11x11") == 3)
	assert(count11("111") == 1)
	assert(count11("1111") == 2)
	assert(count11("1") == 0)
	assert(count11("") == 0)
	assert(count11("hi") == 0)
	assert(count11("11x111x1111") == 4)
	assert(count11("1*111") == 1)
	assert(count11("1hello1") == 0)
	assert(count11("Hello") == 0)
	print("Passed.")

def testStringClean():
	print("testing stringClean...", end="")
	assert(stringClean("yyzzza") == "yza")
	assert(stringClean("abbbcdd") == "abcd")
	assert(stringClean("Hello") == "Helo")
	assert(stringClean("XXabcYY") == "XabcY")
	assert(stringClean("112ab445") == "12ab45")
	assert(stringClean("HelloBookkeeper") == "HeloBokeper")
	print("Passed.")

def testCountHi2():
	print("testing countHi2...", end="")
	assert(countHi2("ahixhi") == 1)
	assert(countHi2("ahibhi") == 2)
	assert(countHi2("xhixhi") == 0)
	assert(countHi2("hixhi") == 1)
	assert(countHi2("hixhhi") == 2)
	assert(countHi2("hihihix") == 3)
	assert(countHi2("xhihihix") == 2)
	assert(countHi2("xxhi") == 0)
	print("Passed.")

def testParenBit():
	print("testing parenBit...", end="")
	assert(parenBit("xyz(abc)123") == "(abc)")
	assert(parenBit("x(hello)") == "(hello)")
	assert(parenBit("(xy)1") == "(xy)")
	assert(parenBit("not really (possible)") == "(possible)")
	assert(parenBit("(abc)") == "(abc)")
	assert(parenBit("(abc)xyz") == "(abc)")
	assert(parenBit("(abc)x") == "(abc)")
	assert(parenBit("(x") == "")
	assert(parenBit("()") == "()")
	assert(parenBit("res(ipsa)louitor") == "(ipsa)")
	assert(parenBit("hello (not really) there") == "(not really)")
	assert(parenBit("ab(ab)ab") == "(ab)")
	assert(parenBit("") == "")
	assert(parenBit("  ) (") == "")
	print("Passed.")

def testNestParen():
	print("testing nestParen...", end="")
	assert(nestParen("(())") == True)
	assert(nestParen("((()))") == True)
	assert(nestParen("((uu))") == False)
	assert(nestParen("())))") == False)
	assert(nestParen("(((e()urgergb)") == False)
	print("Passed.")

testNestParen()