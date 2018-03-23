
def groupSum(start, nums, target):
	if (target == 0): return True
	if (start == len(nums)): return False
	else:
		return groupSum(start+1,nums,target-nums[start])\
			or groupSum(start+1,nums,target)

def groupSum6(start, nums, target):
	if (start == len(nums)): return target == 0
	if (nums[start] == 6):
		return groupSum6(start+1,nums,target-6)
	else:
		return groupSum6(start+1,nums,target) or \
			groupSum6(start+1, nums, target-nums[start])

def groupNoAdj(start, nums, target):
	if (start >= len(nums) and target != 0): return False
	if (target == 0): return True
	else:
		return groupNoAdj(start+2,nums,target-nums[start]) \
			or groupNoAdj(start+1,nums,target)

def groupSum5(start, nums, target):
	if (start >= len(nums)): return target == 0
	if (nums[start] % 5 == 0):
		if (start+1 < len(nums) and nums[start+1] == 1):
			return groupSum5(start+2,nums,target-nums[start])
		else:
			return groupSum5(start+1,nums,target-nums[start])
	else:
		return groupSum5(start+1,nums,target) or \
			groupSum5(start+1,nums,target-nums[start])

def groupSumClump(start, nums, target):
	if (start >= len(nums) and target != 0): return False
	if (start == len(nums) and target == 0): return True
	if (start < len(nums)-1 and nums[start] == nums[start+1]):
		return groupSumClump(start+2, nums, target) \
			or groupSumClump(start+2, nums, target-2*nums[start])

	else:
		return groupSumClump(start+1, nums, target) \
			or groupSumClump(start+1, nums, target-nums[start])

def splitArray(nums):
	return splitSum(0,nums,0,0)

def splitSum(start, nums, sum1, sum2):
	if (start >= len(nums) and sum1 != sum2): return False
	if (start == len(nums) and sum1 == sum2): return True
	else:
		return splitSum(start+1,nums,sum1+nums[start],sum2) \
			or splitSum(start+1,nums,sum1,sum2+nums[start])

def splitOdd10(nums):
	return splitSum2(0,nums,0,0)

def splitSum2(start, nums, sum1, sum2):
	if (start == len(nums)):
		if (sum1%10==0) and (sum2%2==1): return True
		else: return False
	else:
		return splitSum2(start+1,nums,sum1+nums[start],sum2) \
			or splitSum2(start+1,nums,sum1,sum2+nums[start])

def split53(nums):
	return foo(0,nums,0,0)

def foo(start, nums, sum1, sum2):
	if (start >= len(nums) and sum1 != sum2): return False
	if (start == len(nums) and sum1 == sum2): return True
	if (nums[start]%5==0):
		return foo(start+1,nums,sum1+nums[start],sum2)
	if (nums[start]%3 == 0) and (nums[start]%5 != 0):
		return foo(start+1,nums,sum1,sum2+nums[start])
	else:
		return foo(start+1,nums,sum1+nums[start],sum2) \
			or foo(start+1,nums,sum1,sum2+nums[start])
### END ###

### TEST FUNCTIONS ###

def testGroupSum():
	print("testing groupSum...", end="")
	assert(groupSum(0, [2,4,8], 10))
	assert(groupSum(0, [2,4,8], 14))
	assert(not groupSum(0, [2,4,8], 9))
	assert(groupSum(0, [10, 2, 2, 5], 9))
	print("Passed.")

def testGroupSum6():
	print("testing groupSum6...", end="")
	assert(groupSum6(0, [5,6,2], 8))
	assert(not groupSum6(0, [5,6,2], 9))
	assert(not groupSum6(0, [5,6,2], 7))
	assert(groupSum6(0, [6,6,6,8], 26))
	print("Passed.")

def testGroupNoAdj():
	print("testing groupNoAdj...", end="")
	assert(groupNoAdj(0, [2,5,10,4], 12))
	assert(not groupNoAdj(0, [2,5,10,4], 14))
	assert(not groupNoAdj(0, [2,5,10,4], 7))
	assert(groupNoAdj(0, [1], 1))
	assert(groupNoAdj(0, [], 0))
	assert(groupNoAdj(0, [9], 0))
	assert(groupNoAdj(0, [5,10,4,1], 11))
	print("Passed.")

def testGroupSum5():
	print("testing groupSum5...", end="")
	assert(groupSum5(0, [2,5,10,4], 19))
	assert(groupSum5(0, [2,5,10,4], 17))
	assert(not groupSum5(0, [2,5,10,4], 12))
	assert(not groupSum5(0, [3,5,1], 4))
	assert(groupSum5(0, [3,5,1], 5))
	assert(groupSum5(0, [1,3,5], 5))
	assert(not groupSum5(0, [3,5,1], 9))
	assert(not groupSum5(0, [2,5,10,4], 7))
	assert(groupSum5(0, [2,5,10,4], 15))
	assert(groupSum5(0, [1], 1))
	assert(not groupSum5(0, [9], 1))
	assert(groupSum5(0, [9], 0))
	assert(groupSum5(0, [], 0))
	print("Passed.")

def testGroupSumClump():
	print("testing groupSumClump...", end="")
	assert(groupSumClump(0, [2,4,8], 10))
	assert(groupSumClump(0, [1,2,4,6,1], 14))
	assert(not groupSumClump(0, [2,4,4,8], 14))
	assert(groupSumClump(0, [8,2,2,2,1], 7))
	assert(not groupSumClump(0, [8,2,2,1], 11))
	assert(groupSumClump(0, [1], 1))
	assert(not groupSumClump(0, [9], 1))
	assert(not groupSumClump(0, [0,2,2,2,2,1], 6))
	print("Passed.")

def testSplitArray():
	print("testing splitArray...", end="")
	assert(splitArray([2,2]))
	assert(splitArray([]))
	assert(not splitArray([1]))
	assert(not splitArray([2,3]))
	assert(splitArray([2,3,5]))
	assert(splitArray([2,5,3]))
	assert(splitArray([2,2,10,10,1,1]))
	assert(not splitArray([1,2,2,10,10,1,1]))
	print("Passed.")

def testSplitOdd10():
	print("testing splitOdd10...", end="")
	assert(splitOdd10([5,5,5]))
	assert(not splitOdd10([5,5,6]))
	assert(splitOdd10([5,5,6,1]))
	assert(splitOdd10([6,5,5,1]))
	assert(splitOdd10([6,5,5,1,10]))
	assert(not splitOdd10([6,5,5,5,1]))
	assert(splitOdd10([1]))
	assert(not splitOdd10([]))
	assert(splitOdd10([10,7,5,5]))
	assert(not splitOdd10([10,0,5,5]))
	assert(splitOdd10([10,7,5,5,2]))
	assert(not splitOdd10([10,7,5,5,1]))
	print("Passed.")

def testSplit53():
	print("testing split53...", end="")
	assert(split53([1,1]))
	assert(not split53([1,1,1]))
	assert(split53([2,4,2]))
	assert(not split53([2,2,2,1]))
	assert(split53([3,3,5,1]))
	assert(not split53([3,5,8]))
	assert(split53([2,4,6]))
	assert(split53([3,5,6,10,3,3]))
	print("Passed.")

def testAll():
	testGroupSum()
	testGroupSum6()
	testGroupNoAdj()
	testGroupSum5()
	testGroupSumClump()
	testSplitArray()
	testSplitOdd10()
	testSplit53()
	print("Passed all!")

testAll()