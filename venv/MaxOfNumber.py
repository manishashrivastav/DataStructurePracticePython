# number =[10, 11, 32 , 34 , 5 , 98 , 12]
#
# def maximum(number , begin , end ):
#
#      max = number[begin]
#      if begin == end:
#          return (number[begin])
#      if end == begin+1:
#          if number[end] > number[begin]:
#              return (number[end])
#          else:
#              return(number[begin])
#      else :
#          mid = int((begin + end)/2)
#          a = maximum(number , begin , mid )
#          b = maximum(number, mid , end )
#          if a >b :
#              return a
#          else:
#              return  b
#
# print(maximum(number, 0 , len(number)-1))
#
def maxNumber(data, length):
    print(">> maxNumber executed with length[{}]".format(length))

    if length == 1:
        print(">> maxNumber returned {} with length[{}]".format(data[0], length))
        return data[0]
    else:
        num = maxNumber(data, length - 1)

    if num > data[length - 1]:
        print(">> maxNumber returned with length[{}]".format(length))
        return num
    else:
        print(">> maxNumber returned with length[{}]".format(length))
        return data[length - 1]


numbers = [10, 11, 12]
print(">> Max is:", maxNumber(numbers, len(numbers)))

"""
def fun1():

    # Recursion
    # fun1()
    # InDirect Recursion
    fun2()

    print(">> fun1")
    # Tail Recursion
    # fun1()

def fun2():

    # fun1()
    fun2()

    print(">> fun2")
"""

# HW: Implement Recursion in Insertion Sort Algorithm