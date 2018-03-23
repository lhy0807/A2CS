def binarySearch(L, target):      
    start = 0
    end = len(L) - 1         
    while(start <= end):
        middle = (start + end)//2
        if(L[middle] == target): 
            return True
        elif(L[middle] > target): 
            end = middle-1
        else: 
            start = middle+1
    return False