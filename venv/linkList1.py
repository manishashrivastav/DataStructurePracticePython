class Product:
    def __init__(self , title , rating , price , dealOfDay , isPrime , deliveryDate , index ,nextProduct):
        self.title= title
        self.rating= rating
        self.price= price
        self.dealOfDay = dealOfDay
        self.isPrime= isPrime
        self.deliveryDate= deliveryDate
        self.index = index
        self.nextProduct= nextProduct
        
class Node:
    def __init__(self, data , nextNode):
        self.data  = data
        self.nextNode = nextNode

class LinkedList:

    head = None
    tail = None
    __size = 0

    def append(self,object):
        # LinkedList.__size+=1
        # node = Node(object, None)
        # print("[Append] Node",node ,"Next Node " ,node.nextNode)
        # if LinkedList.head == None:
        #     LinkedList.head = node
        #     LinkedList.tail=node
        #     print("LinkedList.head",LinkedList.head , "LinkedList.head.nextNode",LinkedList.head.nextNode)
        #     print(LinkedList.tail)
        #     print()
        # else:
        #     LinkedList.tail.nextNode = node
        #     print("LinkedList.tail.nextNode",LinkedList.tail.nextNode)
        #     LinkedList.tail= node
        #     print("LinkedList.tail",LinkedList.tail)
        #     print()
        # print("append")
        # print("LinkedList.__size ",LinkedList.__size )
        product = Product(object[0],object[1], object[2], object[3], object[4] , object[5],LinkedList.__size, None)
        print("[Append] Product", product, "Next product ", product.nextProduct)
        LinkedList.__size += 1

        if LinkedList.head == None:
            LinkedList.head = product
            LinkedList.tail = product
            print("LinkedList.head", LinkedList.head, "LinkedList.head.nextProduct", LinkedList.head.nextProduct)
            # print(LinkedList.tail.nextProduct)
            # print()

        else:

            # print(LinkedList.tail.nextProduct)
            LinkedList.tail.nextProduct=product
            # print(  LinkedList.tail , LinkedList.tail.nextProduct)
            LinkedList.tail=product
            # print(LinkedList.tail , LinkedList.tail.nextProduct)
            # print("added", product.index)
            # self.updateIndex(product.nextProduct)


    def appendBeg(self , object):
        # print("appendBeg")
        LinkedList.__size+=1
        product = Product(object[0],object[1], object[2], object[3], object[4] , object[5], 0 , None)
        # LinkedList.head.nextProduct=LinkedList.head
        temp = LinkedList.head
        LinkedList.head=product
        product.nextProduct=temp
        print("LinkedList.head", LinkedList.head, "LinkedList.head.nextProduct", LinkedList.head.nextProduct)
        self.updateIndex(product.nextProduct)

    def updateIndex(self , product):
        temp = product
        if temp!= None:
            while temp.nextProduct != None:
                temp.index +=1
                temp=temp.nextProduct

            temp.index+=1

    def appendAfterIndex(self , object , index1 ):
        # print("appendAfterIndex")
        LinkedList.__size += 1
        product = Product(object[0], object[1], object[2], object[3], object[4], object[5], index1 + 1, None)
        temp = LinkedList.head
        var = 0
        while var !=LinkedList.__size:
            var+=1
            # print(var)
            if temp.index == index1:
                hash = temp.nextProduct

                temp.nextProduct = product
                product.nextProduct=hash
                if hash ==None:
                    LinkedList.tail == product
                    # print("LLLLLLLLLLLLLLLLLLLLLL",LinkedList.tail)
                # print(product.nextProduct)
                self.updateIndex(product.nextProduct)
                break
            temp = temp.nextProduct

    def remove(self , object):
        LinkedList.__size -= 1

        temp = LinkedList.head
        previous = LinkedList.head
        while temp.nextProduct !=None:
            if temp.title == object[0]:
                previous.nextProduct = temp.nextProduct
                del (temp)
                self.updateDelIndex(previous.nextProduct)
                break
            previous = temp
            temp = temp.nextProduct

    def updateDelIndex(self , product):
        temp = product
        while temp.nextProduct != None:
            temp.index -= 1
            temp = temp.nextProduct

        temp.index -= 1

    def removeHead(self):
        LinkedList.__size -= 1
        temp = LinkedList.head.nextProduct
        del(LinkedList.head)
        LinkedList.head = temp
        self.updateDelIndex(LinkedList.head)

    def removeTail(self):
        LinkedList.__size -= 1
        temp = LinkedList.head
        previous = None
        while temp.nextProduct!= None:
            previous = temp
            temp = temp.nextProduct
        LinkedList.tail = previous
        previous.nextProduct = None
        del (temp)


    def removePosition(self , index):
        pass

    def insert(self , object , index):

        LinkedList.__size += 1
        product = Product(object[0], object[1], object[2], object[3], object[4], object[5], index, None)
        temp = LinkedList.head
        while temp.nextProduct != None:
            if temp.index == index-1:
                hash = temp.nextProduct
                temp.nextProduct = product
                product.nextProduct = hash
                self.updateIndex(product.nextProduct)
                break
            temp = temp.nextProduct

    def printList(self):

        temp = LinkedList.head
        print()
        while temp.nextProduct is not None:
            # print(temp)
            print("({}){} \n{} Rating \nRs {} \nDeal Of the Day {} \nPrime Offer {} \nPosssible Delivery Date {} "
                  .format(temp.index,temp.title , temp.rating , temp.price , temp.dealOfDay , temp.isPrime , temp.deliveryDate))
            # print("/////////", temp.nextProduct)

            temp = temp.nextProduct
            print()
        # print(temp)
        print("({}){} \n{} Rating \nRs {} \nDeal Of the Day {} \nPrime Offer {} \nPosssible Delivery Date {} "
              .format(temp.index ,temp.title, temp.rating, temp.price, temp.dealOfDay, temp.isPrime, temp.deliveryDate))
        # print("/////////", temp.nextProduct)

    def size(self):
        return LinkedList.__size

    def selectionSort(self):

        current = LinkedList.head

        while current != None:

            temp = current.nextProduct
            x = current

            while temp != None:
                if x.price > temp.price:
                    x = temp
                temp = temp.nextProduct

            # Swapping of data
            vT = current.title
            vR = current.rating
            vP = current.price
            vD = current.dealOfDay
            vI = current.isPrime
            vDD = current.deliveryDate

            current.title =x.title
            current.rating =x.rating
            current.price =x.price
            current.dealOfDay = x.dealOfDay
            current.isPrime =x.isPrime
            current.deliveryDate =x.deliveryDate

            x.title = vT
            x.rating = vR
            x.price = vP
            x.dealOfDay = vD
            x.isPrime = vI
            x.deliveryDate = vDD

            # to go to next node
            current = current.nextProduct

        self.printList()


#object of Link List
# lRef = LinkedList()
# lRef.append(85)
# lRef.append(80)
# lRef.append(55)
# lRef.append(78)
#
#
# lRef.printList()
#
# print(">> Size of Linked List is:" ,lRef.size())
pRef = LinkedList()
pRef.append(["Iphone7" ,4 , 78000, "Yes", "No" , "24 January 2020" ])
pRef.append(["Iphone8s" ,5 , 88000, "Yes", "Yes" , "25 January 2020" ])
pRef.append(["IphoneXR" ,3 , 46000, "Yes", "No" , "23 January 2020" ])
pRef.append(["Iphone11 Pro" ,5 , 115000, "Yes", "Yes" , "28 January 2020" ])

pRef.appendBeg(["Iphone11" ,3 , 56000, "Yes", "No" , "30 January 2020" ])

pRef.appendAfterIndex(["Iphone7s" ,5 , 90000, "Yes", "No" , "20 January 2020" ] , 3 )
#
pRef.insert(["Iphone5s" ,5 , 10000, "Yes", "No" , "21 January 2020" ] , 2 )
pRef.append(["Iphone12 Pro" ,5 , 115000, "Yes", "Yes" , "28 January 2020" ])

# print("******************************************************************************************")

# pRef.printList()
# print(">> Size of Linked List is:" ,pRef.size())

# print("####################After Deleting#######################")
pRef.remove(["Iphone7s" ,5 , 90000, "Yes", "No" , "20 January 2020" ])
pRef.remove(["Iphone12 Pro" ,5 , 115000, "Yes", "Yes" , "28 January 2020" ])
pRef.removeHead()
pRef.removeTail()
# pRef.printList()
# print(">> Size of Linked List is:" ,pRef.size())
# #
pRef.appendAfterIndex(["Iphone77s" ,5 , 90000, "Yes", "No" , "20 January 2020" ] , 3)
pRef.appendBeg(["Iphone11" ,3 , 56000, "Yes", "No" , "30 January 2020" ])
pRef.append(["Iphone1199 Pro" ,5 , 115000, "Yes", "Yes" , "28 January 2020" ])
pRef.append(["Iphone1166 Pro" ,5 , 115000, "Yes", "Yes" , "28 January 2020" ])
# print("####################After Adding#######################")
pRef.selectionSort()
# pRef.printList()
# print(">> Size of Linked List is:" ,pRef.size())


# Order of inserting the element in the link list is O(1)
# order of printing the element in the link list is O(n)