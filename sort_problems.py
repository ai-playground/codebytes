from codebytes.sort import merge_sort, quick_sort


def intersection_sorted_arrays(array_1, array_2):
    """
    array_1 = [11,22,33,44,55]
    array_2 = [11,33]
    result = [11, 33]

    array_1 = [11,22,33,44,55]
    array_2 = [11,11]
    result = [11]
    """
    result = []

    left_idx = 0
    right_idx = 0
    
    if array_1[left_idx] < array_2[right_idx]:
        left_array = array_1
        right_array = array_2
    else:
        left_array = array_2
        right_array = array_1
    
    left_length = len(left_array)
    right_length = len(right_array)
    print(left_array)
    print(right_array)
    while True:
        print("left_idx: {}, right_idx: {}".format(left_idx, right_idx))
        while (left_idx < left_length and right_idx < right_length and left_array[left_idx] <= right_array[right_idx]):
            print("here is left array: {}".format(left_array[left_idx]))
            if left_array[left_idx] == right_array[right_idx]:
                result.append(left_array[left_idx])
            left_idx += 1
        print("left_idx: {}, right_idx: {}".format(left_idx, right_idx))
        while (left_idx < left_length and right_idx < right_length and right_array[right_idx] <= left_array[left_idx]):
            print("here is right array:{}".format(right_array[right_idx]))
            if left_array[left_idx] == right_array[right_idx]:
                result.append(left_array[left_idx])
            right_idx += 1

        print("left_idx: {}, right_idx: {}".format(left_idx, right_idx))
        if not (left_idx < left_length and right_idx < right_length):
            break

    return result


if __name__ == "__main__":
    test_array = [22, 55, 11, 44, 33]
    test_array_2 = [11, 22, 33, 55, 44]
    test_array_3 = [11, 33, 55]
    test_array_sorted = merge_sort(test_array)
    test_array_sorted_2 = merge_sort(test_array_2)
    test_array_sorted_3 = merge_sort(test_array_3)
    #print(test_array_sorted)
    #print(test_array_sorted_2)
    print(intersection_sorted_arrays(test_array_sorted_3, test_array_sorted_2))
