from functools import reduce


def prod(lst):
    def mul(x, y):
	    return x*y
    return reduce(mul, lst)


def fn(x, y):
    return x*10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	
	
def str2float(s):

    n = 0
    for i in range(len(s)):
	    if s[i] == '.':
		    n = i
    s1 = reduce(fn, map(char2num, s[:n]))
    s2 = reduce(fn, map(char2num, s[n+1:len(s)]))
    f = s1 + s2*(10**(n+1-len(s)))
    return f 
	

    