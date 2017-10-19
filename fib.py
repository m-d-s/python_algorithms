#!/usr/bin/env python2

def rec_fib(n):
    if(n < 2):
        return 0
    if(n == 2):
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)

def itr_fib(n):
    current  = 0
    next_one = 1 
    if(n > 1):
        for x in range(1, n):
            temp = current + next_one
            current = next_one
            next_one = temp
    return current
    
