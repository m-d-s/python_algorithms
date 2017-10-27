#!/usr/bin/env python2

from copy import deepcopy
from math import (
    log,
    floor
)
from utils.utils import (
    array_is_sorted,
    swap_array_elements
)


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
            swap_array_elements(array, i, i-1)
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
        iterations = int(floor(log(length, 2))) + 1

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
    left = low
    right = mid
    merged = []

    while(length > 0):
        if(left < mid and (right >= high or array[left] <= array[right])):
            merged.append(array[left])
            left += 1
        else:
            merged.append(array[right])
            right += 1
        length -= 1

    for dest, src in zip(range(low, high), range(0, (high-low))):
        array[dest] = merged[src]


# HeapSort
def heap_sort(array):
    heapify(array)
    for i in range(len(array) - 1, -1, -1):
        array[0], array[i] = array[i], array[0]
        down_heap(array, i)
    return array


def heapify(array):
    for i in range(1, len(array)):
        parent = parent_index(i)
        while(parent >= 0 and array[i] > array[parent]):
            array[parent], array[i] = array[i], array[parent]
            i = parent
            parent = parent_index(i)


def down_heap(array, size):
    curr = 0
    child_idx = larger_child_index(array, curr, size)
    while(child_idx < size and array[curr] < array[child_idx]):
        array[curr], array[child_idx] = array[child_idx], array[curr]
        curr = child_idx
        child_idx = larger_child_index(array, curr, size)


def larger_child_index(array, i, last):
    larger_child = last
    left = i * 2 + 1
    right = left + 1
    if(not(left >= last and right >= last)):
        if (right >= last or array[left] > array[right]):
            larger_child = left
        else:
            larger_child = right
    return larger_child


def parent_index(i):
    return int(floor((i - 1) / 2))
