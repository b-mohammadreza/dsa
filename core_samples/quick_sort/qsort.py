#!/usr/bin/python

def qsort(arr: list) -> list:
    """ returns partitioned list.
    Sorts in ascending order. """

    # TODO: What if the list elements are instances of a specific class?
    # In that case how to compare two instances of the class?
    if len(arr) < 1:
        return [] 

    if len(arr) == 1:
        return arr 

    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

        return arr

    pivot_index = 0

    # Put all values less than pivot value to the left of pivot_index 
    index = 0
    while index < len(arr):
        if arr[index] < arr[pivot_index] and index > pivot_index:
            arr[index], arr[pivot_index] = arr[pivot_index], arr[index]
            pivot_index = index

        index += 1 

    # Put all values greater than pivot value to the right of pivot_index 
    index = 0
    while index < len(arr):
        if arr[index] > arr[pivot_index] and index < pivot_index:
            arr[index], arr[pivot_index] = arr[pivot_index], arr[index]
            pivot_index = index

        index += 1

    left_partition:list = qsort(arr[:pivot_index + 1])
    right_partition:list = qsort(arr[pivot_index + 1:])

    new_arr = []
    new_arr.extend(left_partition)
    new_arr.extend(right_partition)

    return new_arr


if __name__ == '__main__':
    pass