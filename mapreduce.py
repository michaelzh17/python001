#!/usr/bin/env python3

def normalize(name):
    m=[]
    #n=''
    m.append(name[0].upper())
    for i in range(1, len(name)):
        m.append(name[i].lower())
    n=''.join(m)
    return n