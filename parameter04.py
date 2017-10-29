#!/usr/bin/env python3

#key word parameter

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

    

# name key word parameter
def person_name(name, age, *, city, major):
    print(name, age, city, major)

    
#parameter combo
def combo(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def combo02(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)


    
    
    
    