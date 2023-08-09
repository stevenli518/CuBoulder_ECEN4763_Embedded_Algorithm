"""This module is for the merge sort."""

# Citation: Adapted from GeeksforGeeks
# pylint: disable = R0801
# pylint: disable = R0903


class MergeSort:
    """Class implementation for MergeSort."""

    def __init__(self):
        """Construct the mergesort data structure."""
        self.array = []

    def sort(self, array):
        """Merge sort the array passed in the argument."""
        if len(array) == 0:
            return True
        self.array = array
        old_type = type(array[0])
        for j in range(1, len(array)):
            new_type = type(array[j])
            if new_type != old_type:
                return False
        self.array = mergesort_helper(array, 0, len(array)-1)
        return True


def merge_helper(array, left, middle, right):
    """Merge function."""
    length_l = middle-left+1
    lenght_r = right-middle

    left_ary = [0] * length_l
    right_ary = [0] * lenght_r

    for i in range(length_l):
        left_ary[i] = array[left+i]
    for i in range(lenght_r):
        right_ary[i] = array[middle+i+1]
    i, j, k = 0, 0, left
    while i < length_l and j < lenght_r:
        if left_ary[i] < right_ary[j]:
            array[k] = left_ary[i]
            i += 1
        else:
            array[k] = right_ary[j]
            j += 1
        k += 1
    while i < length_l:
        array[k] = left_ary[i]
        i += 1
        k += 1
    while j < lenght_r:
        array[k] = right_ary[j]
        j += 1
        k += 1
    return array


def mergesort_helper(array, left, right):
    """Merge sort function."""
    if left < right:

        middle = left + (right-left) // 2
        mergesort_helper(array, left, middle)
        mergesort_helper(array, middle+1, right)
        return merge_helper(array, left, middle, right)
    return array


def get_time_complexity():
    """Get the time complexity of the data structure."""
    return 'O(nlog(n))'


def get_space_complexity():
    """Get the space complexity of the data structure."""
    return 'O(N)'
