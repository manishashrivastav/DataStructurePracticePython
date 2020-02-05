# def isHavingPair(numbers , sum):
#     hasTrue = None
#     for i in range (0 , len(numbers)):
#
#         for j in range (i+1 , len(numbers)):
#             if numbers[i] + numbers[j] == sum:
#                 print(numbers[i] ,"+", numbers[j] , "=" , sum)
#                 hasTrue = True
#                 break
#             else:
#                 hasTrue =False
#           if hasTrue:
#               break
#     return hasTrue


def isHavingPair(numbers, sum):
    hasTrue = False
    diff = set()
    for i  in range(0, len(numbers)):

        if numbers[i] in diff:
            print(hash(numbers[i]))
            hasTrue = True
            break
        else :
            value = sum - numbers[i]
            diff.add(value)
    return hasTrue


numbers1=[6, 2, 3, 9 , 5]
numbers2= [1, 2, 4,4 , 6]
sum =8
print(isHavingPair(numbers1 , sum))
print(isHavingPair(numbers2 , sum))

# Complexity : O(n2)



