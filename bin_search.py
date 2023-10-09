from array import *
def arr(len):
    a = array('i',[])
    n = len

    for i in range(n):
        q = int(input())
        a.append(q)
        
    return a


def bin_search(a, x):
    n = len(a)
    left = -1
    right = n
    while right - left > 1:
        middle = (left + right) // 2
        if a[middle] >= a[middle-1]: # практически единственная строка, которая меняется от задачи к задаче
            right = middle
        else:
            left = middle
    if right != n and a[right] == x: # ответ лежит в right
        return a[right]
    else:
        return False
    
    
print(bin_search(arr(4),1))