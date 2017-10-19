#!/usr/bin/env python2

from utils.test_fixtures import *
from sort import *

print "Test Bubble Sort:"
sort_test(bubble_sort)

print "Test Insertion Sort:"
sort_test(insertion_sort)

print "Test Selection Sort:"
sort_test(selection_sort)

print "Test Top Down Merge Sort:"
sort_test(top_down_merge_sort)

print "Test Bottom Up Merge Sort:"
sort_test(btm_up_merge_sort)
