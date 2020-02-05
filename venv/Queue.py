class Product:
    def __init__(self,pid ,  name, price , quantity=1):
        self.name = name
        self.pid = pid
        self.price = price
        self.quantity = quantity


    def showProduct(self):
        print("{} | {} | {} ".format(self.pid, self.name , self.price))



class Queue:
    size = 0
    total=0
    item =0


    def __init__(self):
        self.head = None
        self.current=None


    def add(self , object):
        Queue.size+=1

        object.next = None
        object.previous = None
        Queue.total += (object.price * object.quantity)
        Queue.item += object.quantity

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


    def iterate(self):
        temp = self.head

        while temp.next != self.head:
            temp.showProduct()
            temp = temp.next

        temp.showProduct()

    def poll(self):
        Queue.size -= 1
        # manage other variables

        print(">> Deleting Node:")
        self.head.showProduct()
        print("~~~~~~~~~~~~~~~~~")
        # temp = self.head
        self.head = self.head.next
        self.head.previous = self.current
        self.current.next = self.head



qRef = Queue()
print(">> qRef is:", qRef)
print(">> Dictionary of qRef is:", qRef.__dict__)

print()

# p1 = Product(101, "AlphaBounce Shoe", 8000)
# qRef.add(p1)
qRef.add(Product(101, "AlphaBounce Shoe", 8000))
qRef.add(Product(201, "iPhone X", 70000 , 2))
qRef.add(Product(301, "Samsung LED", 50000))
qRef.add(Product(401, "Samsung M10", 1000))
qRef.add(Product(501, "Lays", 20 , 10))

qRef.poll()
qRef.poll()
qRef.iterate()

print(">> Queue SIZE:", Queue.size)
print(">> Queue ITEMS:", Queue.item)
print(">> Queue TOTAL PRICE:", Queue.total)

