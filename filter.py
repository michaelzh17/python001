def _odd_iter():
    n = 1
    while True:
	    n = n + 2
	    yield n 
		

		
def _not_divisible(n):
    return lambda x: x % n > 0
	

	
def primes():
    yield 2
    it = _odd_iter()
    while True:
	    n = next(it)
	    yield n 
	    it = filter(_not_divisible(n), it)

		

def is_palindrome(n):
    if n == int(str(n)[::-1]):
	    return n 
    else:
        return None
	
	
	
def by_name(t):
    keys = []
    for i in t:
	    keys.append(i[0])
    return keys
	
def by_score(t):
    keys = []
    for i in t:
        keys.append(i[1])
    return keys
	
	
	
	
	
	
	
