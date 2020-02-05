# def insertionSort(data):
#     print("insertion Sort")
#     iterartion = 0
#     for i in range(1 , len(data)):
#         key = data[i]
#         j = i-1
#         while j>=0 and data[j] > key:
#             data[j+1] = data[j]
#             j-=1
#         data[j+1] = key
#
#     return (data)
#
# numbers = [45 , 22 , 11 , 23 , 19 , 10 , 33 , 12 , 55 , 66]
# print(insertionSort(numbers))

class Node:

    def __init__(self, data, index, nextNode):
        self.data = data
        self.index = index
        self.nextNode = nextNode

    def showNode(self):
        print("{} | {}".format(self.index, self.data))


class LinkedList:

    # Is Property of Class
    head = None
    tail = None
    __size = 0

    def append(self, object):


        node = Node(object, LinkedList.__size, None)

        print(">> [APPEND] Node:", node, "[NEXT NODE]:", node.nextNode)

        LinkedList.__size += 1

        if LinkedList.head is None:
            LinkedList.head = node
            LinkedList.tail = node
            print(">> [APPEND] LinkedList.head:", LinkedList.head, "[NEXT NODE]:", LinkedList.head.nextNode)
            print(">> [APPEND] LinkedList.tail:", LinkedList.tail)

        else:
            LinkedList.tail.nextNode = node
            print(">> [APPEND] LinkedList.tail.nextNode:",  LinkedList.tail.nextNode)
            LinkedList.tail = node
            print(">> [APPEND] LinkedList.tail:", LinkedList.tail)

        print()

    def updateIndexes(self, node):
        temp = node

        while temp.nextNode is not None:
            temp.index += 1
            temp = temp.nextNode

        temp.index += 1


    def appendBeginning(self, object):


        node = Node(object, 0, None)
        print(">> [APPEND] Node:", node, "[NEXT NODE]:", node.nextNode)

        LinkedList.__size += 1

        temp = LinkedList.head
        LinkedList.head = node
        node.nextNode = temp

        print(">> [APPEND] LinkedList.head:", LinkedList.head, "[NEXT NODE]:", LinkedList.head.nextNode)

        self.updateIndexes(node.nextNode)

        print()

    def insert(self, index, object):

        LinkedList.__size += 1

        node = Node(object, index, None)
        print(">> [APPEND] Node:", node, "[NEXT NODE]:", node.nextNode)

        temp = LinkedList.head
        previous = LinkedList.head

        while temp.nextNode is not None:

            if temp.index == index:

                node.nextNode = previous.nextNode
                previous.nextNode = node

                self.updateIndexes(node.nextNode)

                break

            previous = temp
            temp = temp.nextNode

        print()

    def printList(self):

        temp = LinkedList.head

        while temp.nextNode is not None:
            temp.showNode()
            temp = temp.nextNode

        temp.showNode()

    def printNode(self , node):
        if node.nextNode==None:
            node.showNode()
            return
        else:
            node.showNode()
            self.printNode(node.nextNode)


    def size(self):
        return LinkedList.__size


    def selectionSort(self):

        current = LinkedList.head

        while current != None:

            temp = current.nextNode
            x = current

            while temp != None:
                if x.data > temp.data:
                    x = temp
                temp = temp.nextNode

            #Swapping of data
            v1 = current.data
            current.data = x.data
            x.data = v1

            # to go to next node
            current = current.nextNode

        self.printList()

    def binarySearch(self , element ,begin , end):
        mid = (begin + end) // 2

        if numbers[mid] == element:
            print("element found at {} position ".format(mid))

        elif numbers[mid] > element and mid != 0:
            binarySearch(numbers, element, begin, mid - 1)

        elif numbers[mid] < element and mid != len(numbers) - 1:
            binarySearch(numbers, element, mid + 1, end)

        else:
            print("element not found")

    # def insertionSort(self):
    #     node = LinkedList.head.nextNode
    #     current = LinkedList.head
    #
    #     while node.nextNode!=None:
    #         key = node.data
    #
    #         while current.nextNode !=node.nextNode:
    #             if current.data> node.data:
    #
    #
    #             # temp = temp.nextNode


"""
    def insertionSort(self):

        sortedListHead = None
        copy = None
        current = LinkedList.head
        s =0
        while s!=LinkedList.__size:
            s += 1
            sortedListHead = self.selfRecursive(sortedListHead , current , copy)
            current = current.nextNode


        LinkedList.head = sortedListHead
        current.nextNode=None
        self.printList()

    def selfRecursive(self , sortedListHead , current , copy):
        if sortedListHead == None and copy ==None:
            sortedListHead = current
            copy = current
            return sortedListHead
        else:

                if sortedListHead.data > current.data:

                    temp = sortedListHead
                    temp2 = sortedListHead.nextNode
                    sortedListHead = current
                    sortedListHead.nextNode = temp
                    return sortedListHead

"""
lRef = LinkedList()
lRef.append(85)
lRef.append(80)
lRef.append(55)
lRef.append(78)
lRef.append(90)
lRef.append(9)

lRef.appendBeginning(106)
lRef.appendBeginning(12)
lRef.insert(2, 777)
lRef.append(22)

lRef.printNode(LinkedList.head)
print()
print("After Selection Sort")
lRef.selectionSort()

element = 75
begin=lRef.head.index
end = lRef.tail.index
lRef.binarySearch(element ,begin , end )