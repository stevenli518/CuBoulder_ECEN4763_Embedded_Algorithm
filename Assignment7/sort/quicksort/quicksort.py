"""This module is for the merge sort."""
# Citation: Adapted from GeeksforGeeks
# pylint: disable = R0903


class QuickSort:
    """Class implementation for MergeSort."""

    def __init__(self):
        """Construct the data structure."""
        self.array = []

    def sort(self, array):
        """Sort the array passed in the argument."""
        if len(array) == 0:
            return True
        self.array = array
        old_type = type(array[0])
        for i in range(1, len(array)):
            temp_type = type(array[i])
            if temp_type != old_type:
                return False
        self.array = quicksort_helper(array, 0, len(array)-1)
        return True


def partition(array, left, right):
    """Partition function."""
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
    temp = array[right]
    array[right] = array[i+1]
    array[i+1] = temp
    return i+1


def quicksort_helper(array, left, right):
    """Quicksort helper function."""
    if left < right:
        partitioning_index = partition(array, left, right)
        quicksort_helper(array, left, partitioning_index-1)
        quicksort_helper(array, partitioning_index+1, right)
    return array


def get_time_complexity():
    """Get the time complexity of the data structure."""
    return 'O(nlog(n))'


def get_space_complexity():
    """Get the space complexity of the data structure."""
    return 'O(N)'
