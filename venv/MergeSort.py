def mergeSort(numbers):
    # left = []
    # right = []
    # if len(numbers)!=1:
    #     mid = (0 + len(numbers)-1)//2
    #
    #     for i in range(0 , mid):
    #         left.append(numbers[i])
    #         print(left)
    #
    #         mergeSort(left)
    #
    #     for j in range(mid , len(numbers)):
    #         right.append(numbers[j])
    #         print(right)
    #
    #         mergeSort(right)


    if len(numbers) < 2:
        return numbers

    mid = len(numbers) // 2

    left_sequence = mergeSort(numbers[:mid])
    print("Left",left_sequence)

    right_sequence = mergeSort(numbers[mid:])
    print("Right",right_sequence)

    return merge(left_sequence, right_sequence)

def merge(left, right):
    print("Left Array " , left)
    print("Right Array" , right)
    """
    Traverse both sorted sub-arrays (left and right), and populate the result array
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result

numbers = [-3 , 10 , 14 , -9 , 11 , 13]
print(mergeSort(numbers))
# print(numbers)
