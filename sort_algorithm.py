#в данном файле будут лежать алгоритмы сортировок
from elementary_operations import *


def my_insertion_sort(my_array):
    n = len(my_array)

    for i in range(n):
        j = i
        while (j > 0) and (my_array[j] < my_array[j-1]):
            my_array[j], my_array[j-1] = my_array[j-1], my_array[j]

    return my_array


def my_merge(left_array, right_array):
    i = 0
    j = 0
    left_lenth = len(left_array)
    right_lenth = len(right_array)
    merge_array = []

    while (i < left_lenth) or (j < right_lenth):
        if (j == right_lenth) or ((left_lenth > i) and (left_array[i] < right_array[j])):
            merge_array.append(left_array[i])
            i += 1
        else:
            merge_array.append(right_array[j])
            j += 1

    return merge_array


def my_merge_sort(my_array):
    my_array_lenth = len(my_array)
    if my_array_lenth < 2:
        return my_array

    middle_ind = my_array_lenth//2
    left_array = my_merge_sort(my_array[:middle_ind])
    right_array = my_merge_sort(my_array[middle_ind:])

    return my_merge(left_array, right_array)






