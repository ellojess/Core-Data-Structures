#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


    if array[0] == item:
        return index
    elif len(array) > 1:
        return linear_search_recursive(array[1:], item, index + 1)
    else:
        return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    """
    find middle of array and see if item is there
    compare if item is larger or smaller than middle of array, change middle accorddingly
    keep looping until item is found
    """
    first = 0 
    last = len(array) - 1 
    found = False

    while(first <= last and not found):
        mid = (first + last)//2
        if array[mid] == item:
            found = True
        else:
            if item < array[mid]:
                last = mid - 1
            else: 
                first = mid + 1 
    return found


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests