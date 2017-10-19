#!/usr/bin/env python2

from utils.test_fixtures import test_equal
from fib import *


first_ten_fib_digits = [0,1,1,2,3,5,8,13,21,34];

print "Test rec_fib"

for x in range(0,10):
    test_equal(first_ten_fib_digits[x], rec_fib(x + 1))

print "Test itr_fib"
for x in range(0,10):
    test_equal(first_ten_fib_digits[x], itr_fib(x + 1))
