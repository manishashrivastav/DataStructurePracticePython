def insertionSort(data , i ):

    key = data[i]
    j = i-1

    sort(j , data , key)

    if i+1 <= len(data)-1:
        insertionSort(data , i+1)

    return (data)

def sort(j , data , key):

    if data[j]>key:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key

    if j>=0 and data[j]>key:
        sort(j , data , key)


numbers = [111 ,45 , 22 , 11 , 23 , 19 ,109, 10 , 33 , 12 , 55 , 66]
# numbers=[120 , 56 , 6]
print(insertionSort(numbers , 1 ))