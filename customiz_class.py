#customization class


class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
		
    def __getattr__(self, attr):
        if attr == 'age':
            return 99 
        if attr == 'score':
            return lambda: 78
	
    def __call__(self):
        print('My name is %s.' % self.name)
		


    __repr__ = __str__
	

	
	

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a
	
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b 
        return a

        
		
		


