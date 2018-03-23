def bubbleSort(a):
    n = len(a)
    end = n
    swapped = True
    while (swapped):
        swapped = False
        for i in range(1, end):
            if (a[i-1] > a[i]):
                swap(a, i-1, i)
                swapped = True
        end -= 1
