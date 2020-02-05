class Product:
    def __init__(self,pid ,  name, price , quantity=1):
        self.name = name
        self.pid = pid
        self.price = price
        self.quantity = quantity


    def showProduct(self):
        print("{} | {} | {} ".format(self.pid, self.name , self.price))



class Stack:
    size = 0
    total=0
    item =0


    def __init__(self):
        self.head = None
        self.current=None


    def push(self , object):
        Stack.size+=1

        object.next = None
        object.previous = None
        Stack.total += (object.price * object.quantity)
        Stack.item += object.quantity

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

    def pop(self):
        if self.head.previous!=self.head:
            Stack.size-=1
            temp = self.current
            self.current = temp.previous
            self.head.previous = self.current
            self.current.next = self.head

            del temp
        else:
            self.head=None
            self.current=None





    def iterate(self):
        if self.head!=None:
            temp = self.current
            while temp.previous != self.current:
                temp.showProduct()
                temp = temp.previous
            temp.showProduct()
        else:
            print("Stack is Empty")

sRef = Stack()
print(">> sRef is:", sRef)
print(">> Dictionary of sRef is:", sRef.__dict__)

print()

# p1 = Product(101, "AlphaBounce Shoe", 8000)
# sRef.push(p1)
sRef.push(Product(101, "AlphaBounce Shoe", 8000))
sRef.push(Product(201, "iPhone X", 70000 , 2))
sRef.push(Product(301, "Samsung LED", 50000))
sRef.push(Product(401, "Samsung M10", 1000))
sRef.push(Product(501, "Lays", 20 , 10))

sRef.pop()
sRef.pop()
sRef.pop()
sRef.pop()
sRef.pop()


sRef.iterate()

print(">> Stack SIZE:", Stack.size)
print(">> Stack ITEMS:", Stack.item)
print(">> Stack TOTAL PRICE:", Stack.total)

