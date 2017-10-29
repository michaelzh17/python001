#!/usr/bin/env python3

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)
    
    

def enroll_deft(name, gender, age=7, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:',age)
    print('city:',city)
    
    

def add_end_static(L=None):
    if L is None:
        L=[]
    L.append('End')
    return L



def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

# dynamic parameter
def calc_dyn(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum



    













