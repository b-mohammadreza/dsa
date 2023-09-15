#!/usr/bin/python

def msort(arr: list) -> list:
    """ Sorts the elements in ascending order """

    if len(arr) == 0:
        return []
 
    if len(arr) == 1:
        return arr

    mid_index = (len(arr) - 1) // 2

    left_arr = msort(arr[:mid_index + 1])
    right_arr = msort(arr[mid_index + 1:])

    if len(left_arr) == 0:
        return right_arr
    
    if len(right_arr) == 0:
        return left_arr

    # merge:
    temp_arr = []

    if left_arr[-1] <= right_arr[0]:
        temp_arr.extend(left_arr)
        temp_arr.extend(right_arr)
        return temp_arr

    if right_arr[-1] <= left_arr[0]:
        temp_arr.extend(right_arr)
        temp_arr.extend(left_arr)
        return temp_arr

    primary_arr = []
    seconday_arr = []
    if left_arr[0] < right_arr[0]:
        temp_arr.append(left_arr[0])

        primary_arr = left_arr
        seconday_arr = right_arr

    else:
        temp_arr.append(right_arr[0])

        primary_arr = right_arr
        seconday_arr = left_arr

    sec_index = 0
    for prim_index in range(1, len(primary_arr)):
        while sec_index < len(seconday_arr) and seconday_arr[sec_index] <= primary_arr[prim_index]:
            temp_arr.append(seconday_arr[sec_index])
            sec_index += 1

        temp_arr.append(primary_arr[prim_index])

    if sec_index < len(seconday_arr):
        temp_arr.extend(seconday_arr[sec_index:])

    return temp_arr

if __name__ == '__main__':
    pass