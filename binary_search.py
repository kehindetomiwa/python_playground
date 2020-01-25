def binary_search(data, target, low, high):
    '''' Return True if target is found
         search only look at the portion of
         data[low] to data[high] inclusive
    '''
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

alist = [2,2,3,4,5,10,20,33,7]
alist.sort()
low, high = 0, len(alist)-1
print(binary_search(alist, 1, low, high))
