# Multi-inheritage

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass
	
class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

		
		
class Pig(Mammal, RunnableMixIn):
    pass

class Duck(Bird, FlyableMixIn):
    pass
	
	
	
	
	
