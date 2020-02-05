def binary(num ):
        if num == 1:
            print(1)

        else:
            binary(num//2)
            print(num % 2 , end=" ")
binary(6)
