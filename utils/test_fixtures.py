#!/usr/bin/env python2
from collections import namedtuple
from random import randint
from sys import maxint
from copy import deepcopy

def test_equal(a, b):
    if(a == b):
        print "PASSED"
    else:
        print "FAILED"

ArraysForSort = namedtuple('ArraysForSort', ['sorted_array', 'unsorted_array']);

def arrays_for_sort_test(length):
    #max_int = maxint
    unsorted_array = []
    for x in range(0, length):
        max_int = length
        unsorted_array.append(randint(0, max_int))
    sorted_array = deepcopy(unsorted_array)
    sorted_array.sort()
    return ArraysForSort(sorted_array, unsorted_array)

def sort_test(sort_fn):
    successes = []
    for i in range(0, 100):
        arrays = arrays_for_sort_test(i)
        result = sort_fn(arrays.unsorted_array)
        successes.append(1 if arrays.sorted_array == result else 0)
    print ("PASSED" if all(successes) else "FAILED")
