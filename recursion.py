#!/usr/bin/env python3

# factorial 
def fact(n):
    s=1
    while n > 0:
        s = s * n
        n = n-1
    return s


#factorial using recursion
def fact_re(n):
    if n==1:
        return 1
    return n*fact_re(n-1)


#Hanoi
#1. n-1 should be in the middle rod
#2. move the biggest piece to the third rod
#3. move the n-1 from the middle rod to the third rod

#move to middle rod
def move_a(n, a, b, c):
    if n=1:
        print('A-->C')
    else:
        move(n-1, a, b, c)
        print('A-->B')

        
def first_move(n, a, b, c):
    if n = 2 
def move(n, a, b, c):
    if n==2:
        print('A --> C')
        print('A --> B')
        print('C --> B')
    else:
        move(n-1, a, b, c)
        print('A --> C')
        
    
    
    if n==3:
        print('A --> B')
        print('A --> C')
        print('B --> C')
        print('A --> B')
        print('C --> A')
        print('C --> B')
        print('A --> B')
    if n > 3:
        
        
    return move(n-1, a, b, c) 
        
        
        
    