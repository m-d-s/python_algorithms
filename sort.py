#!/usr/bin/env python2

from copy import deepcopy
from math import log, floor
def array_is_sorted(array):
    end = len(array) - 1
    
    for i in range(0, end):
        if(array[i] > array[i+1]):
            return False
    
    return True

def swap_array_elements(array, first_idx, second_idx):
    if(first_idx != second_idx):
        temp = array[first_idx]
        array[first_idx] = array[second_idx]
        array[second_idx] = temp

def bubble_sort(array):
    end = len(array) - 1
    
    while(not array_is_sorted(array)):
        for i in range(0, end):
            if(array[i] > array[i+1]):
                swap_array_elements(array, i, i+1)
    
    return array

def insertion_sort(array):
    end = len(array)
    
    for i in range(0, end):
        while(i > 0 and array[i] < array[i-1]):
            swap_array_elements(array, i , i-1)
            i -= 1
    
    return array

def selection_sort(array):
    end = len(array)
    
    for i in range(0, end):
        min_index = i
        for j in range(i, end):
            if(array[j] < array[min_index]):
                min_index = j
        swap_array_elements(array, i, min_index)
    
    return array

def top_down_merge_sort(array):
   length = len(array)
   if(length > 1):
       copy = deepcopy(array)
       return top_down_split(copy, 0, length, array)
   else:
       return array

def top_down_split(array_a, beg, end, array_b):
    if(end - beg < 2):
        return 
    mid = beg + ((end - beg) / 2)
    top_down_split(array_b, beg, mid, array_a)
    top_down_split(array_b, mid, end, array_a)
    top_down_merge(array_a, beg, mid, end, array_b)
    return array_b

def top_down_merge(array_a, beg, mid, end, array_b):
    i = beg
    j = mid
    
    for k in range(beg, end):
        if(i < mid and (j >= end or array_a[i] <= array_a[j])):
            array_b[k] = array_a[i]
            i += 1
        else:
            array_b[k] = array_a[j]
            j += 1

def btm_up_merge_sort(array):
    length = len(array)
    if(length > 1):
        iterations = int(floor(log(length,2))) + 1
        
        for exp in range(1, iterations):
            width = 2**exp
            for low in range(0, length, width):
                high = low + width
                mid = int(floor((low + high) / 2))
                if(high > length):
                    high = length
                btm_up_merge(array, low, mid, high)
    
        btm_up_merge(array, 0, low, high)
    return array

def btm_up_merge(array, low, mid, high):
    length = high - low
    l = low
    r = mid
    merged = []

    while(length > 0):
        if(l < mid and (r >= high or array[l] <= array[r])):
            merged.append(array[l])
            l+=1
        else:
            merged.append(array[r])
            r+=1
        length-=1
    
    for dest, src in zip(range(low, high), range(0,(high-low))):
        array[dest] = merged[src]
