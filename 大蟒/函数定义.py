# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    try:
        d= b*b-4*a*c;
        n1=(math.sqrt(d)-b)/(2*a);
        n2=(-math.sqrt(d)-b)/(2*a);
        return n1,n2
    except ValueError as e:
        print('无解')

n1=int(input('n1='))
n2=int(input('n2='))
n3=int(input('n3='))
print(quadratic(n1,n2,n3))
