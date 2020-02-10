class Product:
    def __init__(self,pid ,  name, price , quantity=1):
        self.name = name
        self.pid = pid
        self.price = price
        self.quantity = quantity


    def showProduct(self):
        print("{} | {} | {} ".format(self.pid, self.name , self.price))

class LinkList:
    size = 0
    total=0
    item =0

    def __init__(self):
        self.head = None
        self.current=None

    def appendStarting(self , object):
        LinkList.size+=1

        object.next = None
        object.previous = None
        LinkList.total += (object.price * object.quantity)
        LinkList.item += object.quantity

        if self.head==None:
            self.head=object
            self.current=object

        else:
            self.current.next = object
            object.previous = self.current
            self.current = object
            self.current.next = self.head
            self.head.previous = self.current
        print(">> NEXT {} PREVIOUS {}".format(object.next, object.previous))

    def appendBegin(self , object):
        temp = self.head
        self.head=object
        self.head.next=temp
        self.head.previous=self.current
        self.current.next=self.head


    def binarySearch(self , sort):

        pass

    def linearSearch(self , name):
        temp = self.head

        while temp.next != self.head:
            if temp.name == name:
                print("Product Found")
                temp.showProduct()
                break
            temp=temp.next

        if temp.name == name:
            print("Product Found")
            temp.showProduct()


    def InsertionSort(self):
        pass

    def SelectionSort(self ):
        temp = self.head
        sTemp = self.head.next

        while temp.next != self.head:
            if temp.price > sTemp.price:
                var = sTemp
            if sTemp.next != self.head:
                sTemp = sTemp.next
            else:
                if var!=None:

                    vP = temp.pid
                    vN = temp.name
                    vPr = temp.price

                    temp.pid = var.pid
                    temp.name =var.name
                    temp.price = var.price

                    var.pid = vP
                    var.name = vN
                    var.price = vPr
                    print(temp.price, var.price)

                temp=temp.next
                var = None



    def iterateForward(self):

        temp = self.head
        i=0
        j=0


        # while temp.next != self.head:
        #     temp.showProduct()
        #     temp = temp.next
        #
        # temp.showProduct()
        while i != LinkList.size:
            # while j!= LinkList.size-i-1:
            #     if temp.price > temp.next.price:

            temp.showProduct()
            temp = temp.next
            i+=1

        # temp.showProduct()

    def iterateBackward(self):
        temp = self.current
        while temp.previous != self.current:
            temp.showProduct()
            temp = temp.previous
        temp.showProduct()

    def deleteFromEnd(self):

        LinkList.size -= 1
        temp = self.current
        self.current = temp.previous
        self.head.previous = self.current
        self.current.next = self.head

        del temp


    def deleteFromBeg(self):

        LinkList.size -= 1
        # manage other variables

        print(">> Deleting Node:")
        self.head.showProduct()
        print("~~~~~~~~~~~~~~~~~")
        # temp = self.head
        self.head = self.head.next
        self.head.previous = self.current
        self.current.next = self.head

    def deleteInBetween(self , data):

        LinkList.size -= 1
        temp = self.head
        while temp.next != self.head:
            if temp.pid == data:
                var = temp.previous
                var2 = temp.next
                var.next = temp.next
                var2.previous = temp.previous
                del temp
                break
            temp = temp.next

    def BubbleSort(self):
        itemp = self.head
        jtemp = self.head
      

        for i in range(0, LinkList.size):
            for j in range(0, LinkList.size-i-1):

                if jtemp.price > jtemp.next.price:

                    vP = jtemp.pid
                    vN = jtemp.name
                    vPr = jtemp.price

                    jtemp.pid = jtemp.next.pid
                    jtemp.name = jtemp.next.name
                    jtemp.price = jtemp.next.price

                    jtemp.next.pid = vP
                    jtemp.next.name = vN
                    jtemp.next.price = vPr


                jtemp = jtemp.next
            itemp = itemp.next
            jtemp = self.head

lRef = LinkList()
print(">> lRef is:", lRef)
print(">> Dictionary of lRef is:", lRef.__dict__)

print()
# p1 = Product(101, "AlphaBounce Shoe", 8000)
# lRef.appendStarting(p1)
lRef.appendStarting(Product(101, "AlphaBounce Shoe", 8000))
lRef.appendStarting(Product(201, "iPhone X", 70000 , 2))
lRef.appendStarting(Product(301, "Samsung LED", 50000))
lRef.appendStarting(Product(401, "Samsung M10", 100000))
lRef.appendStarting(Product(501, "Lays", 20 , 10))

# lRef.iterateForward()
# lRef.iterateBackward()
# lRef.deleteFromEnd()
# lRef.deleteFromBeg()
# lRef.deleteInBetween(201)
# print("###########")
# lRef.iterateForward()
#
# print(">> LINKED LIST SIZE:", LinkList.size)
# print(">> LINKED LIST ITEMS:", LinkList.item)
# print(">> LINKED LIST TOTAL PRICE:", LinkList.total)

# lRef.SelectionSort()
# lRef.iterateForward()
# lRef.linearSearch("Lays")
# print()
# lRef.appendBegin(Product(601, "Laptop", 2 , 70000))
# lRef.iterateForward()
# lRef.binarySearch(lRef.SelectionSort())
lRef.BubbleSort()
# lRef.iterateBackward()
lRef.iterateForward()
