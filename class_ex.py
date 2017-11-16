#class examples


class Animal(object):
    def run(self):
        print('animal is running...')

		
		
class Dog(Animal):
    def run(self):
        print('Dog is running...')

		
class Pig(Animal):
    def run(self):
        print('Pig is running...')
		
class Puppy(Dog):
    def run(self):
        print('Puppy is running...')

class PuPig(Pig):
    def run(self):
        print('Pupig is running...')
		
		

class Student(object):
    count = 0
	
    __slots__ = ('name', 'age')

    def __init__(self, name):
        self.name = name
        Student.count =Student.count + 1
		
class Teacher(object):
    pass

	
	
	
class Officer(object):
    
    @property
    def score(self):
        return self._score
    
	
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
		
		
	
class Screen(object):
    @property
    def width(self):
	    return self._width
    @width.setter
    def width(self, value):
        self._width = value
	
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height





