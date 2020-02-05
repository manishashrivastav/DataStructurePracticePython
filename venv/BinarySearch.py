def binarySearch(numbers ,  element , begin , end):
    mid = (begin+end)//2

    if numbers[mid] == element:
        print("element found at {} position ".format(mid))

    elif numbers[mid] > element and mid!=0:
        binarySearch(numbers , element , begin , mid-1)

    elif numbers[mid] < element and mid!= len(numbers)-1:
        binarySearch(numbers , element , mid+1 , end)

    else:
        print("element not found")

numbers=[1,2,3,4,5,6,7,8,9,10]
element = 2
binarySearch(numbers ,  element , 0 , len(numbers)-1)

