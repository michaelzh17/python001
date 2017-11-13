#!/usr/bin/env python3

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n+1
    return 'done'


def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a+b
        n = n+1
    return 'done'


#杨辉三角

def triangles():
    lst = []
    
    #generate first list
    n = 1
    lst.append(1)
    yield lst
    
    #generate second list
    n = n + 1
    lst.append(1)
    yield lst 
    
    #generate more list
    while True:
        n = n + 1
        #make a copy of the current list
        lst_cp = lst.copy()
        #empty the current list
        lst = []
        #make list
        lst.append(1)
        for i in range(1, n-1):
            lst.append(lst_cp[i-1] + lst_cp[i])
        lst.append(1)
        yield lst
        
        

def triangles_01():
    L = [1]
    while 1:
        yield L
        L=[1]+[L[i] + L[i+1] for i in range(len(L)-1)]+[1]
        
        
def triangles_02():
    L = [1]
    while True:
        yield L
        L.insert(0, 0)    #首尾添加一个0，便于循环计算
        L.append(0)
        L = [L[i] + L[i + 1] for i in range(len(L)-1)] 
            
        
    
    









