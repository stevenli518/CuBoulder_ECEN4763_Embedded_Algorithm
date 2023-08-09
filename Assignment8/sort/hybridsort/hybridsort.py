"""This module is for the Tim sort."""
# Citation: Adapted from GeeksforGeeks


def insertionsort(array, left, right):
    """Insetionsort."""
    for i in range(left+1, right+1):
        j = i
        while j > left and array[j-1] > array[j]:  # [j-1, j]
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1


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


def minrun(length):
    """Calculate the minrun."""
    i = 0
    while length >= 32:
        i = i | length & 1
        length = length >> 1
    return length + i


class HybridSort:
    """Class implementation for HybridSort."""

    def __init__(self):
        """Construct the data structure."""
        self.array = []

    def sort(self, array):
        """Sort the array passed in the argument."""
        self.array = array
        for i in range(1, len(array)):
            old = type(array[i-1])
            new = type(array[i])
            if old != new:
                return False
        length = len(array)
        minrun_num = 32
        for left in range(0, length, minrun_num):
            right = min(left + minrun_num - 1, length - 1)
            insertionsort(array, left, right)
        temp = minrun_num
        while temp < length:
            for left in range(0, length, 2 * temp):
                middle = min(left + temp - 1, length - 1)
                right = min(left + 2 * temp - 1, length - 1)
                if middle < right:
                    merge_helper(array, left, middle, right)
            temp *= 2
        self.array = array
        return True

    def get_sorted_list(self):
        """Return the sorted array."""
        return self.array


def get_time_complexity():
    """Get the time complexity of the data structure."""
    return 'O(nlogn)'


def get_space_complexity():
    """Get the space complexity of the data structure."""
    return 'O(n)'
