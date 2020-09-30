import unittest
#from memory_profiler import memory_usage


def selection_sort(array):
    """Sorts a list of numbers using selection sort.

    The input list is assumbed to consists of only numbers.

    Args:
        array: A python list of numbers.

    Returns:
        A list of sorted numbers.

    Raises:
        None.
    """
    start_index = 0
    end_index = len(array)
    for row in range(start_index, end_index):
        min_index = row
        for col in range(row, end_index):
            if array[col] < array[min_index]:
                min_index = col
        array[row], array[min_index] = array[min_index], array[row]
    return array


def insertion_sort(array):
    """Sorts a list of numbers using insertion sort.

    The input list is assumbed to consists of only numbers.

    Args:
        array: A python list of numbers.

    Returns:
        A list of sorted numbers.

    Raises:
        None.
    """
    start_index = 1
    end_index = len(array)
    for row in range(start_index, end_index):
        element_index = row
        element = array[element_index]
        true_element_index = row-1
        while (true_element_index >= 0) and (element < array[true_element_index]):
            array[true_element_index+1] = array[true_element_index]
            true_element_index = true_element_index-1
        array[true_element_index+1] = element
    return array


def merge_sort(array):
    """Merges two sorted arrays at mid-point into one sorted array.

    The input list is assumed to consists of only numbers.

    Args:
        array: A python list of numbers.

    Returns:
        A list of sorted numbers.

    Raises:
        None.
    """
    low = 0
    high = len(array)-1
    # driver_program for merge sort
    merge_sort_helper(array, low, high)
    return array


def merge_sort_helper(array, low, high):
    """Helper function for merge sort.

    The input list is assumed to consists of only numbers.

    Args:
        array: A python list of numbers.
        low: low index within range of [0,len(array)]
        high: high index within range of [0,len(array)]

    Returns:
        None.

    Raises:
        None.
    """
    # empty list or singleton list
    if(low >= high):
        return
    else:
        # divide the array into two-halves
        # when number of elements is even, 
        # left array and right array have equal number of elements
        # when number of elements is odd, 
        # left array has one element less than that of right array
        mid = (low + high)//2
        # divide the array at mid point
        # sort left and right arrays
        merge_sort_helper(array, low, mid)
        merge_sort_helper(array, mid+1, high)
        # merge two sorted arrays aka left and right arrays
        merge(array, low, high, mid)
    return


def merge(array, low, high, mid):
    """Merges two sorted arrays at mid-point into one sorted array.

    The input list is assumed to consists of only numbers.

    Args:
        array: A python list of numbers.
        low: low index within range of [0,len(array)]
        high: high index within range of [0,len(array)]
        mid: low index within range of [0,len(array)]

    Returns:
        A list of sorted numbers.

    Raises:
        None.
    """
    # create a local copy of array for merging the left and right arrays
    array_copy = array[:]
    # create three indexes for iteration purpose
    # one for left copy, one for right copy
    # and one more for merged array
    index = low
    index_1 = low
    index_2 = mid+1
    # We will compare each element in left copy with that of right copy
    # untill we run of elements in either of them and add them
    while((index_1 <= mid) and (index_2 <= high)):
        if(array_copy[index_1] <= array_copy[index_2]):
            array[index] = array_copy[index_1]
            index += 1
            index_1 += 1
        else:
            array[index] = array_copy[index_2]
            index += 1
            index_2 += 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while(index_1 <= mid):
        array[index] = array_copy[index_1]
        index += 1
        index_1 += 1

    while(index_2 <= high):
        array[index] = array_copy[index_2]
        index += 1
        index_2 += 1
    return


def quick_sort(array):
    """Merges two arrays using quick sort algorithm.

    The input list is assumed to consists of only numbers.

    Args:
        array: A python list of numbers.

    Returns:
        A list of sorted numbers.

    Raises:
        None.
    """
    low = 0
    high = len(array)-1
    # driver_program for merge sort
    quick_sort_helper(array, low, high)
    return array


def quick_sort_helper(array, low, high):
    """A helper function to recursively implement quick sort.

    The input list is assumed to consists of only numbers.

    Args:
        array: A python list of numbers.

    Returns:
        None.

    Raises:
        None.
    """
    if low >= high:
        return
    pivot_index = chose_pivot(array, low, high)
    partition_index = partition(array, low, high, pivot_index)
    quick_sort_helper(array, low, partition_index-1)
    quick_sort_helper(array, partition_index+1, high)
    return


def chose_pivot(array, low, high):
    """
    [22, 44, 55, 33, 11]
    low = 0
    high = 4
    pivot_index
    """
    middle = low+high//2

    if array[low] > array[middle]:
        array[low], array[middle] = array[middle], array[low]
    if array[middle] > array[high]:
        array[high], array[middle] = array[middle], array[high]
    if array[low] > array[middle]:
        array[low], array[middle] = array[middle], array[low]
    return middle


def partition(array, low, high, pivot_index):
    """
    [22, 44, 55, 33, 11]
    low = 0
    high = 4
    pivot_index = 3 i.e element = 33
    """
    pivot = array[pivot_index]
    array[high], array[pivot_index] = array[pivot_index], array[high]
    left = low
    right = high-1

    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        else:
            break

    partition_index = left
    array[partition_index], array[high] = array[high], array[partition_index]
    return partition_index

class sortingTest(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([11, 22, 33, 44]), [11, 22, 33, 44])
        self.assertEqual(selection_sort([22, 11, 33, 44]), [11, 22, 33, 44])
        self.assertEqual(selection_sort([11, 33, 22, 44]), [11, 22, 33, 44])
        self.assertEqual(selection_sort([44, 33, 22, 11]), [11, 22, 33, 44])
        return

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([11, 22, 33, 44]), [11, 22, 33, 44])
        self.assertEqual(insertion_sort([22, 11, 33, 44]), [11, 22, 33, 44])
        self.assertEqual(insertion_sort([11, 33, 22, 44]), [11, 22, 33, 44])
        self.assertEqual(insertion_sort([44, 33, 22, 11]), [11, 22, 33, 44])
        return

    def test_merge_sort(self):
        self.assertEqual(merge_sort([11, 22, 33, 44]), [11, 22, 33, 44])
        self.assertEqual(merge_sort([22, 11, 33, 44]), [11, 22, 33, 44])
        self.assertEqual(merge_sort([11, 33, 22, 44]), [11, 22, 33, 44])
        self.assertEqual(merge_sort([44, 33, 22, 11]), [11, 22, 33, 44])
        return

    def test_quick_sort(self):
        self.assertEqual(quick_sort([11, 22, 33, 44]), [11, 22, 33, 44])
        self.assertEqual(quick_sort([22, 11, 33, 44]), [11, 22, 33, 44])
        self.assertEqual(quick_sort([11, 33, 22, 44]), [11, 22, 33, 44])
        self.assertEqual(quick_sort([44, 33, 22, 11]), [11, 22, 33, 44])
        return


if __name__ == "__main__":
    #test_array = [22,55,11,44,33]
    #insertion_sort(test_array)
    unittest.main()

    #mem_usage = memory_usage(merge)
    #print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
    #print('Maximum memory usage: %s' % max(mem_usage))
