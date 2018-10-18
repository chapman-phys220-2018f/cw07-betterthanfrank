#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Amelia Roseto & Gwyneth Casey & Gabriella Nutt
# Student ID: 2289652
# Email: roseto@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW07
###

"""Classwork 07
This classwork introduces numpy arrays and compares their performance to
python lists.
"""

import math
import numpy as np

def gen_gaussian_list(a, b, n=1000):

    dx = (b-a)/(n-1)
    x = [a + k*dx for k in range(n)]

    def gauss(x):
        return (1/math.sqrt(2*math.pi))*math.exp(-x**2/2)
    g = [gauss(xk) for xk in x]
    return (x, g)

def sinc_list(a, b, n=1000):

    dx = (b-a)/(n-1)
    x = [a + k*dx for k in range(n)]

    def sinc(x):
        if x == 0:
            return 1
        else:
            return (math.sin(x) / x)

    sinc = [sinc(xk) for xk in x]
    return (x, sinc)

def gen_gaussian_array(a, b, n=1000):

    x = np.linspace(a, b, n)

    def gauss(x):
        return (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)

    g = gauss(x)
    return (x, g)

def sinc_array(a, b, n=1000):

    x = np.linspace(a, b, endpoint=True, num=n)

    def sinc(x):
        ones = np.ones_like(x)
        return(np.divide(np.sin(x), x, out = ones, where=x!=0))

    s = sinc(x)
    return (x, s)

def sinf_list(a, b, n=1000):

    dx = (b-a)/(n-1)
    x = [a + k*dx for k in range(n)]
    x = [z for z in x if z != 0]

    def sinf(x):
        return (math.sin(1/x))

    g = [sinf(xk) for xk in x]
    return (x, g)

def sinf_array(a, b, n=1000):

    x = np.linspace(a,b,endpoint=True,num=n)
    g = np.ones_like(x)
    g = np.sin(np.divide(1, x, where=x!=0, out=g))
    return (x, g)

def main(a,b,n=1000):

    x1, g1 = sinc_list(a,b,n)

    for (x1k, g1k) in zip(x1, g1):

        print("({}, {})".format(x1k, g1k))
        
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        n = int(sys.argv[3])
        main(a,b,n)
    elif len(sys.argv) == 3:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        main(a,b)
    else:
        print("Usage: cw07.py a b [n]")
        print("  a : float, lower bound of domain")
        print("  b : float, upper bound of domain")
        print("  n : integer, number of points in domain")
        exit(1)

