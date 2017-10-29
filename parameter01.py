#!/usr/bin/env python3

def power(x):
    return x*x  


def power02(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

# default parameter must point to static object
def add_end(l=[]):
    l.append('END')
    return l


def cal(numbers):
    sum = 0
    for row in numbers:
        sum = sum + row*row
    return sum


def cal_c(*numbers):
    sum = 0
    for row in numbers:
        sum = sum + row*row
    return sum












