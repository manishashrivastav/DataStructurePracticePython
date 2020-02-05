
def selectionSort(numbers , i):

    # for i in range(0 , len(numbers)):
    idx = getMinIdx( numbers , i)
    numbers = swap(i , numbers , idx)
    if i != len(numbers)-1:
        i +=1
        selectionSort(numbers , i)
    return  numbers

        # for j in range (i, len(numbers)):
        #     if c > numbers[j]:
        #         idx = j
        #         c = numbers[j]

        # if idx != i:
        #
        #     temp = numbers[i]
        #     numbers[i] = numbers[idx]
        #     numbers[idx] = temp

def swap(i , numbers , idx):

    temp = numbers[i]
    numbers[i] = numbers[idx]
    numbers[idx] = temp
    return  numbers

def getMinIdx(numbers , i ):
    idx = i
    for j in range(i, len(numbers)):
        if numbers[idx] > numbers[j]:
            idx = j

    return  idx






numbers = [49, 45 , 22 , 11 , 23 , 19 , 47 , 10 , 33 , 12 , 46 , 109 ]
print(selectionSort(numbers , 0))

