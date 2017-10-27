#!/usr/bin/env python2

def array_is_sorted(array):
    end = len(array) - 1
    is_sorted = True

    for i in range(0, end):
        if(array[i] > array[i+1]):
            is_sorted = False
    
    return is_sorted

def swap_array_elements(array, first_idx, second_idx):
    if(first_idx != second_idx):
        temp = array[first_idx]
        array[first_idx] = array[second_idx]
        array[second_idx] = temp


