from array import *
def lin_poisk1():
    a = array('i',[])
    x = int(input())
    n = int(input())

    for i in range(n):
        q = int(input())
        a.append(q)
        
        
    for i in range(n):
        if a[i] == x:
            print(a[i],' ', end = ' ')
            
            
def lin_poisk2():
    a = array('i',[])
    n = int(input())

    for i in range(n):
        q = int(input())
        a.append(q)
        
    max = 0
    for i in range(n):
        if max < a[i]:
            max = a[i]
    
    print(max)
    
def lin_poisk3():
    a = array('i',[])
    n = int(input())

    for i in range(n):
        q = int(input())
        a.append(q)
        
    sum = 0  
    for i in range(n):
        sum+=a[i]
    
    print(sum)
    
def lin_poisk4():
    a = array('i',[])
    n = int(input())

    for i in range(n):
        q = int(input())
        a.append(q)
        
        
    for i in range(n):
        if a[i]%2 == 0:
            print(a[i])
            break
        

lin_poisk4()